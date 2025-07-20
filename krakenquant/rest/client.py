import requests
from krakenquant.auth import KrakenAuth
from .endpoints import BASE_URL, PUBLIC_ENDPOINTS, PRIVATE_ENDPOINTS
from .market import MarketAPI
from .account import AccountAPI

class KrakenRESTClient:
    def __init__(self, api_key: str = None, api_secret: str = None):
        if api_key is None or api_secret is None:
            raise ValueError("API key and secret must be provided")
        
        self.session = requests.Session()
        self.auth = KrakenAuth(api_key, api_secret) if api_key and api_secret else None
        self.market = MarketAPI(self)
        self.account = AccountAPI(self)

    def _url(self, path: str) -> str:
        return f"{BASE_URL}{path}"

    def _get(self, path: str, params: dict = None) -> dict:
        url = self._url(path)
        resp = self.session.get(url, params=params)
        resp.raise_for_status()
        return resp.json()

    def _post(self, path: str, data: dict = None) -> dict:
        url = self._url(path)
        data = data or {}
        headers = self.auth.sign(path, data) if self.auth else {}
        resp = self.session.post(url, headers=headers, data=data)
        resp.raise_for_status()
        return resp.json()

    def public(self, endpoint: str, params: dict = None) -> dict:
        if endpoint not in PUBLIC_ENDPOINTS:
            raise ValueError(f"Unknown public endpoint: {endpoint}")
        return self._get(PUBLIC_ENDPOINTS[endpoint], params)

    def private(self, endpoint: str, data: dict = None) -> dict:
        if not self.auth:
            raise RuntimeError("Private endpoint requires authentication")
        if endpoint not in PRIVATE_ENDPOINTS:
            raise ValueError(f"Unknown private endpoint: {endpoint}")
        return self._post(PRIVATE_ENDPOINTS[endpoint], data)