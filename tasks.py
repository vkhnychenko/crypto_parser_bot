from celery import Celery
import logging
from app import bot
from config import CHAT_ID
import asyncio
from coinsbit_parse import parse_sst
from uniswap_parse import get_sst_sell_price_from_uniswap, get_sst_buy_price_from_uniswap

app = Celery('tasks')
app.config_from_object('config', namespace='CELERY')

app.conf.beat_schedule = {
    'crypto-notification-sst-every-5-minute': {
        'task': 'tasks.sst_notification',
        'schedule': 300
    }
}


async def send_message(msg):
    await bot.send_message(CHAT_ID, msg)


@app.task
def sst_notification():
    coinsbit_data = parse_sst()
    coinsbit_sell_price = coinsbit_data.get('bids').get('average')
    coinsbit_buy_price = coinsbit_data.get('asks').get('average')
    uniswap_buy_price = get_sst_buy_price_from_uniswap()
    uniswap_sell_price = get_sst_sell_price_from_uniswap()
    if coinsbit_sell_price / uniswap_buy_price > 1:
        msg = 'arbitration found uniswap -> coinsbit'
        asyncio.run(send_message(msg))
    elif uniswap_sell_price / coinsbit_buy_price > 1:
        msg = 'arbitration found coinsbit -> uniswap'
        asyncio.run(send_message(msg))
