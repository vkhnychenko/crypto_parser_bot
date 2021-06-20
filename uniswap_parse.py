from uniswap import Uniswap
from config import UNISWAP_PROVIDER, ETH_ADDRESS, PRIVATE_KEY, TOTAL_COIN

version = 3
uniswap = Uniswap(address=ETH_ADDRESS, private_key=PRIVATE_KEY, version=version, provider=UNISWAP_PROVIDER)


# Some token addresses we'll be using later in this guide
eth = "0x0000000000000000000000000000000000000000"
bat = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
dai = "0x89d24A6b4CcB1B6fAA2625fE562bDD9a23260359"
sst = '0x2863916C6ebDBBf0c6f02F87b7eB478509299868'
usdt = '0xdAC17F958D2ee523a2206206994597C13D831ec7'


def get_sst_buy_price_from_uniswap() -> float:
    return uniswap.get_price_output(usdt, sst, TOTAL_COIN * 10 ** 18) / 10 ** 6 / TOTAL_COIN


def get_sst_sell_price_from_uniswap() -> float:
    return uniswap.get_price_input(sst, usdt, TOTAL_COIN * 10**18) / 10**6 / TOTAL_COIN


if __name__ == '__main__':
    print(uniswap.get_price_input(sst, usdt, TOTAL_COIN * 10**18) / 10**6 / TOTAL_COIN)
    print(type(uniswap.get_price_input(sst, usdt, TOTAL_COIN * 10**18) / 10**6 / TOTAL_COIN))
    # print(uniswap._get_eth_token_input_price(sst, 1000*10**18, 3000)/ 10**6)
    print(type(uniswap.get_price_output(usdt, sst, TOTAL_COIN * 10**18) / 10**6 / TOTAL_COIN))
