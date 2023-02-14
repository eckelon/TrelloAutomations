from requests import request

from config.config import api_key, board_id, token, triage_list_id

query = {"key": api_key, "token": token}
headers = {"Accept": "application/json"}


def do_get(url: str):
    return request("GET", url, params=query, headers=headers).json()


def do_post(url, params):
    return request("POST", url, params=params | query, headers=headers).json()


def do_put(url, params):
    return request("PUT", url, params=params | query, headers=headers).json()


def do_delete(url):
    return request("DELETE", url, params=query, headers=headers).json()
