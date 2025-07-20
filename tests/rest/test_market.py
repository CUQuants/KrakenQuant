import pytest
from unittest.mock import MagicMock
from krakenquant.rest.market import MarketAPI

@pytest.fixture
def mock_client():
    client = MagicMock()
    return client

@pytest.fixture
def market(mock_client):
    return MarketAPI(mock_client)

def test_get_server_time(market, mock_client):
    market.get_server_time()
    mock_client.public.assert_called_with('Time')

def test_get_tradable_asset_pairs(market, mock_client):
    market.get_tradable_asset_pairs(['XBTUSD'])
    mock_client.public.assert_called()

def test_get_ticker(market, mock_client):
    market.get_ticker(['XBTUSD'])
    mock_client.public.assert_called_with('Ticker', {'pair': 'XBTUSD'})

def test_get_ohlc(market, mock_client):
    market.get_ohlc('XBTUSD', interval=5)
    mock_client.public.assert_called()

def test_get_order_book(market, mock_client):
    market.get_order_book('XBTUSD', count=10)
    mock_client.public.assert_called()

def test_get_recent_trades(market, mock_client):
    market.get_recent_trades('XBTUSD')
    mock_client.public.assert_called()

def test_get_recent_spreads(market, mock_client):
    market.get_recent_spreads('XBTUSD')
    mock_client.public.assert_called() 