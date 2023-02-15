from typing import Any, Type

from requests import Response, request

from config.config import api_key, token

QueryType: Type[dict[str, str]] = dict[str, str]


query: QueryType = {"key": api_key, "token": token}
headers = {"Accept": "application/json"}


def do_get(url: str) -> Any:
    return request("GET", url, params=query, headers=headers).json()


def do_post(url: str, params: QueryType) -> Response:
    return request("POST", url, params=query | params, headers=headers)


def do_put(url: str, params: QueryType) -> Response:
    return request("PUT", url, params=params | query, headers=headers)


def do_delete(url: str) -> Response:
    return request("DELETE", url, params=query, headers=headers)
