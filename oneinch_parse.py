import requests
from config import INCH_QUOTE_URL, USDT, SST


def get_1inch_price(from_token, to_token, amount_from, decimal_from):
    payload = {
        "fromTokenAddress": from_token,
        "toTokenAddress": to_token,
        "amount": amount_from * 10 ** decimal_from
    }
    try:
        resp = requests.get(INCH_QUOTE_URL, params=payload)
        resp.raise_for_status()
        data = resp.json()
        price_token = int(data["toTokenAmount"]) / 10 ** data["toToken"]["decimals"]
        return amount_from/price_token
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print(get_1inch_price(USDT, SST, 1000, 6))
