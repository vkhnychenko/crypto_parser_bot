from uniswap import Uniswap
from config import UNISWAP_PROVIDER, ETH_ADDRESS, PRIVATE_KEY, TOTAL_COIN, USDT, SST

version = 3
uniswap = Uniswap(address=ETH_ADDRESS, private_key=PRIVATE_KEY, version=version, provider=UNISWAP_PROVIDER)


def get_sst_buy_price_from_uniswap() -> float:
    return uniswap.get_price_output(USDT, SST, TOTAL_COIN * 10 ** 18) / 10 ** 6 / TOTAL_COIN


def get_sst_sell_price_from_uniswap() -> float:
    return uniswap.get_price_input(SST, USDT, TOTAL_COIN * 10**18) / 10**6 / TOTAL_COIN


if __name__ == '__main__':
    print(uniswap.get_price_input(SST, USDT, TOTAL_COIN * 10**18) / 10**6 / TOTAL_COIN)
    print(type(uniswap.get_price_input(SST, USDT, TOTAL_COIN * 10**18) / 10**6 / TOTAL_COIN))
    # print(uniswap._get_eth_token_input_price(sst, 1000*10**18, 3000)/ 10**6)
    print(type(uniswap.get_price_output(USDT, SST, TOTAL_COIN * 10**18) / 10**6 / TOTAL_COIN))
