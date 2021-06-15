import responses

from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}


@mock_http_response(responses.GET, "/api/v3/exchangeInfo", mock_item, 200)
def test_exchange_info():
    """Tests the API endpoint to get exchange info"""

    api = Client()
    response = api.exchange_info()
    response.should.equal(mock_item)
