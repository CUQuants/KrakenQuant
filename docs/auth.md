# Authentication

KrakenQuant uses API key and secret authentication for private REST endpoints.

## How it Works
- Pass your Kraken API key and secret to `KrakenRESTClient`.
- The library signs requests automatically.

## Example
```python
from krakenquant.rest.client import KrakenRESTClient

client = KrakenRESTClient(api_key='YOUR_API_KEY', api_secret='YOUR_API_SECRET')
```

Keep your credentials secure. Never share or commit them. 