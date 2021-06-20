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


#Celery settings
CELERY_TIMEZONE = "Europe/Moscow"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BROKER_URL = 'redis://localhost:6379/0'
