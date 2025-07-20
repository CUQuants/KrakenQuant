
##
## Import KrakenQuant
##
from krakenquant.rest.client import KrakenRESTClient
from krakenquant.rest.account import AccountAPI
from krakenquant.rest.market import MarketAPI

##
## Replace with your Kraken API credentials
##

# API_KEY = 'YOUR_API_KEY'
# API_SECRET = 'YOUR_API_SECRET'
API_KEY = 'neHOnbJqBpbKeoOz/YG/aofsxzricAvP1KTx0xrotxWwzg8RPvFc9iX7'
API_SECRET = 'Qazte/qK6+H1dUT7m010tZFbKk1U8CCkGpx29nIN0v47nT85yQmb1zTxTAhrrxvqwjT3/dkK66hXRhH5TllT9A=='

client = KrakenRESTClient(api_key=API_KEY, api_secret=API_SECRET)


account_api = AccountAPI(client)
balance = account_api.get_account_balance()
print('Account Balance:', balance)


market_api = MarketAPI(client)
ticker = market_api.get_ticker(['XBTUSD'])
print('Ticker Info for XBTUSD:', ticker) 