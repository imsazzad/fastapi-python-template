import asyncio
from asyncio import AbstractEventLoop
from unittest import TestCase
from unittest.mock import patch

from app.util.rest_client_util import RestClientUtil


async def mock_req_get(url, headers):
    return "get response returned"


async def mock_req_post(url, data):
    return "post response returned"


class TestRestClientUtil(TestCase):
    __loop: AbstractEventLoop

    @classmethod
    def setUpClass(cls):
        cls.__loop = asyncio.new_event_loop()

    @classmethod
    def tearDownClass(cls):
        cls.__loop.close()

    @patch('requests_async.get', mock_req_get)
    def test_rest_client_util_rest_get(self):
        response = self.__loop.run_until_complete(RestClientUtil.rest_get("some/path"))
        assert response == "get response returned"

    @patch("requests_async.post", mock_req_post)
    def test_rest_client_util_rest_post(self):
        response = self.__loop.run_until_complete(RestClientUtil.rest_post("some url", "req dto"))
        assert response == "post response returned"
