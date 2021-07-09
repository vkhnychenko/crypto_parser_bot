from celery import Celery
from celery.schedules import crontab
from app import bot
from config import CHAT_ID, USDT, SST
import asyncio
from coinsbit_parse import parse_sst
from uniswap_parse import get_sst_sell_price_from_uniswap, get_sst_buy_price_from_uniswap
from oneinch_parse import get_1inch_price

app = Celery('tasks')
app.config_from_object('config', namespace='CELERY')

app.conf.beat_schedule = {
    'crypto-notification-sst-every-5-minute': {
        'task': 'tasks.sst_notification',
        'schedule': 300
    },
    'crypto-notification-sst-price-every-2-hour': {
        'task': 'tasks.sst_price',
        'schedule': 7200
    }
}


async def send_message(msg):
    await bot.send_message(CHAT_ID, msg, parse_mode='Markdown')


@app.task
def sst_notification():
    coinsbit_data = parse_sst()
    coinsbit_sell_price = coinsbit_data.get('bids').get('average')
    coinsbit_buy_price = coinsbit_data.get('asks').get('average')
    uniswap_buy_price = get_sst_buy_price_from_uniswap()
    uniswap_sell_price = get_sst_sell_price_from_uniswap()
    if coinsbit_sell_price / uniswap_buy_price > 1:
        msg = 'arbitration found uniswap -> coinsbit'
        asyncio.get_event_loop().run_until_complete(send_message(msg))
    elif uniswap_sell_price / coinsbit_buy_price > 1:
        msg = 'arbitration found coinsbit -> uniswap'
        asyncio.get_event_loop().run_until_complete(send_message(msg))


@app.task
def sst_price():
    msg = "*PRICE SST*\n"
    try:
        buy_sst_price_1inch = get_1inch_price(USDT, SST, 1000, 6)
        sell_sst_price_1inch = get_1inch_price(SST, USDT, 1000, 18, sell=True)
        msg += f'_1Inch buy price 1000 USDT:_ *{buy_sst_price_1inch}*\n' \
               f'_1Inch sell price 1000 SST:_ *{sell_sst_price_1inch}*\n'
    except Exception:
        msg += '*1Inch get price error*\n'
    try:
        coinsbit_sst_info = parse_sst()
        buy_sst_coinsbit_price = coinsbit_sst_info.get('asks')['average']
        buy_sst_amount = coinsbit_sst_info.get('asks')['amount']
        sell_sst_coinsbit_price = coinsbit_sst_info.get('bids')['average']
        sell_sst_amount = coinsbit_sst_info.get('bids')['amount']
        msg += f'_Coinsbit buy price {buy_sst_amount} SST:_ *{buy_sst_coinsbit_price}*\n' \
               f'_Coinsbit sell price {sell_sst_amount} SST:_ *{sell_sst_coinsbit_price}*\n'
    except Exception as e:
        msg += '*Coinsbit get price error*\n'

    asyncio.get_event_loop().run_until_complete(send_message(msg))
