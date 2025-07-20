import pytest
from unittest.mock import MagicMock
from krakenquant.rest.account import AccountAPI

@pytest.fixture
def mock_client():
    client = MagicMock()
    return client

@pytest.fixture
def account(mock_client):
    return AccountAPI(mock_client)

def test_get_account_balance(account, mock_client):
    account.get_account_balance()
    mock_client.private.assert_called_with('Balance')

def test_get_trade_balance(account, mock_client):
    account.get_trade_balance(aclass='currency', asset='XBT')
    mock_client.private.assert_called()

def test_get_open_orders(account, mock_client):
    account.get_open_orders(trades=True)
    mock_client.private.assert_called()

def test_add_order(account, mock_client):
    account.add_order('XBTUSD', 'buy', 'limit', 1.0, price=50000)
    mock_client.private.assert_called_with('AddOrder', pytest.ANY)

def test_cancel_order(account, mock_client):
    account.cancel_order('TXID123')
    mock_client.private.assert_called_with('CancelOrder', {'txid': 'TXID123'}) 