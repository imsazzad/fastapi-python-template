import requests_async


class RestClientUtil:

    @staticmethod
    async def rest_get(url: str) -> requests_async.Response:
        response = await requests_async.get(url=url, headers={'Content-Type': 'application/json'})
        return response

    @staticmethod
    async def rest_post(url: str, req_dto: dict) -> requests_async.Response:
        response = await requests_async.post(url=url, data=req_dto)
        return response
