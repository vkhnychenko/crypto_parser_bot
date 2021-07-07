import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(env_path):
    load_dotenv(dotenv_path=env_path)


#TG BOT settings
API_TOKEN = os.getenv('API_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


#Uniswap settings
UNISWAP_PROVIDER = os.getenv('UNISWAP_PROVIDER')
ETH_ADDRESS = os.getenv('ETH_ADDRESS')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
TOTAL_COIN = 400

#COINSBIT
COINSBIT_BASE_URL = 'https://coinsbit.io'
COINSBIT_REQUEST_URL = '/api/v1/public/depth/result'
COINSBIT_API_KEY = os.getenv('COINSBIT_API_KEY')
COINSBIT_API_SECRET = os.getenv('COINSBIT_API_SECRET')


#Celery settings
CELERY_TIMEZONE = "Europe/Moscow"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')

#Tokens contracts
SST = '0x2863916C6ebDBBf0c6f02F87b7eB478509299868'
USDT = '0xdAC17F958D2ee523a2206206994597C13D831ec7'
ETH = "0x0000000000000000000000000000000000000000"
BAT = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
DAI = "0x89d24A6b4CcB1B6fAA2625fE562bDD9a23260359"

#1inch settings
INCH_QUOTE_URL = "https://api.1inch.exchange/v3.0/1/quote"
