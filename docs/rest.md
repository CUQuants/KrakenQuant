# REST API Reference

KrakenQuant provides a simple interface to Kraken's REST API for account management, trading, and market data.

## Main Classes
- `KrakenRESTClient`: Handles authentication and requests.
- `AccountAPI`: Account and trading endpoints.

## Common Methods

### AccountAPI
- `get_account_balance()` — Get account balances.
- `get_trade_balance()` — Get trade balance info.
- `get_open_orders()` — List open orders.
- `get_closed_orders()` — List closed orders.
- `query_orders(txid)` — Query specific orders.
- `add_order(pair, type_, ordertype, volume, ...)` — Place a new order.
- `cancel_order(txid)` — Cancel an order.

See the code and docstrings for full parameter details.

## Example
```python
from krakenquant.rest.client import KrakenRESTClient
from krakenquant.rest.account import AccountAPI

client = KrakenRESTClient(api_key, api_secret)
account = AccountAPI(client)
orders = account.get_open_orders()
``` 