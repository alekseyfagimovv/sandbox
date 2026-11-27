import unittest
from unittest.mock import patch

import requests


def get_usd_rate():
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()
    return data["rates"]["RUB"]

class Test_rate(unittest.TestCase):
    @patch('requests.get')
    def test_rate(self, mock_get):
        mock_get.return_value.json.return_value = {"rates": {"RUB": 92.5}}
        self.assertEqual(get_usd_rate(), 92.5)
        mock_get.assert_called_once_with("https://api.exchangerate-api.com/v4/latest/USD")

unittest.main()

