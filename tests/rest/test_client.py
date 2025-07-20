import pytest
from unittest.mock import patch, MagicMock
from krakenquant.rest.client import KrakenRESTClient

@pytest.fixture
def client():
    return KrakenRESTClient(api_key='key', api_secret='secret')

def test_url_building(client):
    assert client._url('/foo') == 'https://api.kraken.com/foo'

@patch('krakenquant.rest.client.requests.Session.get')
def test_public_get(mock_get, client):
    mock_get.return_value.json.return_value = {'result': 'ok'}
    mock_get.return_value.raise_for_status = lambda: None
    result = client.public('Time')
    assert result == {'result': 'ok'}

@patch('krakenquant.rest.client.requests.Session.post')
def test_private_post(mock_post, client):
    mock_post.return_value.json.return_value = {'result': 'ok'}
    mock_post.return_value.raise_for_status = lambda: None
    result = client.private('Balance')
    assert result == {'result': 'ok'}

@pytest.mark.parametrize('endpoint', ['Time', 'Ticker'])
def test_public_endpoint_validation(client, endpoint):
    # Should not raise for valid endpoints
    client.public(endpoint)

@pytest.mark.parametrize('endpoint', ['Balance', 'TradeBalance'])
def test_private_endpoint_validation(client, endpoint):
    # Should not raise for valid endpoints
    client.private(endpoint)

@pytest.mark.parametrize('endpoint', ['FakeEndpoint'])
def test_public_endpoint_invalid(client, endpoint):
    with pytest.raises(ValueError):
        client.public(endpoint)

@pytest.mark.parametrize('endpoint', ['FakeEndpoint'])
def test_private_endpoint_invalid(client, endpoint):
    with pytest.raises(ValueError):
        client.private(endpoint) 