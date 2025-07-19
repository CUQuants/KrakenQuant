# KrakenQuant
Asynchronous Python library for Kraken's REST and WebSocket APIs, built for CU Quants. Supports secure trading, real-time data, and strategy integration. Lightweight, modular, and designed for internal Trading/Research team.

# Architecture
```
KrakenQuant/
├── krakenquant/
│   ├── __init__.py
│   ├── rest/
│   │   ├── __init__.py
│   │   ├── client.py
│   │   └── endpoints.py
│   ├── websocket/
│   │   ├── __init__.py
│   │   ├── client.py
│   │   ├── handlers.py
│   │   └── message_types.py
│   ├── auth/
│   │   ├── __init__.py
│   │   └── signer.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── time.py
│   └── exceptions.py
├── tests/
│   ├── rest/
│   ├── websocket/
│   └── auth/
├── examples/
│   ├── rest_demo.py
│   └── websocket_demo.py
├── setup.py
├── README.md
└── pyproject.toml

```
