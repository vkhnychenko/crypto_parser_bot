import requests
from functools import reduce
from config import COINSBIT_REQUEST_URL, COINSBIT_BASE_URL, TOTAL_COIN
import logging


def check_total(obj: list):
    amount = 0
    total = 0
    for i in obj:
        logging.info(i)
        total += reduce(lambda x, y: float(x) * float(y), i)
        amount += float(i[1])
        if amount >= TOTAL_COIN:
            break
    return total, amount, total / amount


def parse_sst() -> dict:
    payload = {'market': "SST_USDT", 'limit': 100}
    try:
        resp = requests.get(COINSBIT_BASE_URL + COINSBIT_REQUEST_URL, params=payload)
        resp.raise_for_status()
        data = resp.json()
        asks = data.get('asks')
        bids = data.get('bids')
        asks_total, asks_amount, asks_average = check_total(asks)
        bids_total, bids_amount, bids_average = check_total(bids)
        return {
            'asks': {
                'total': asks_total,
                'amount': asks_amount,
                'average': asks_average
            },
            'bids': {
                'total': bids_total,
                'amount': bids_amount,
                'average': bids_average
            }
        }

    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    print(parse_sst())
