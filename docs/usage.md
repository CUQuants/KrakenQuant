# KrakenQuant Usage Guide

KrakenQuant is a lightweight Python library for interacting with Kraken's REST and WebSocket APIs. This guide covers basic usage to get you started quickly.

## Installation

```bash
pip install .
```

## REST API Example

```python
from krakenquant.rest.client import KrakenRESTClient
from krakenquant.rest.account import AccountAPI

# Initialize REST client
client = KrakenRESTClient(api_key='YOUR_API_KEY', api_secret='YOUR_API_SECRET')
account_api = AccountAPI(client)

# Get account balance
balance = account_api.get_account_balance()
print(balance)
```

## WebSocket API Example

```python
from krakenquant.websocket import KrakenWebSocketClient

ws_client = KrakenWebSocketClient()
ws_client.connect()

# Subscribe to ticker feed
ws_client.subscribe(['ticker'], ['XBT/USD'])
```

## Notes
- Replace `YOUR_API_KEY` and `YOUR_API_SECRET` with your Kraken API credentials.
- See the `examples/` directory for more advanced usage.
- For questions, contact the CU Quants team. 