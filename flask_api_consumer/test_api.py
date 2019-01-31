import requests_mock
import unittest
import json
from api import calculate_aircon_cubic_weight_avg
from mock_response import product_api_responses


class TestProductAPI(unittest.TestCase):

    @requests_mock.mock()
    def test_product_cubic_weight_calculation(self, m):
        fake_host = 'http://anything.com'
        entry_point = '/api/products/1'
        for endpoint, response in product_api_responses.items():
            m.get(endpoint, text=json.dumps(response))
        average_weight = calculate_aircon_cubic_weight_avg(
            {'host': fake_host, 'endpoint': entry_point}
        )
        assert str(average_weight) == '41.6133846875'
