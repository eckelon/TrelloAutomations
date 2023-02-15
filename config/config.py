from typing import Any

import tomli

api_key: str = ""
token: str = ""
board_id: str = ""
triage_list_id: str = ""

with open("config/env.toml", mode="rb") as fp:
    config: dict[str, Any] = tomli.load(fp)
    auth_opts: dict[str, str] = config["auth"]
    board_opts: dict[str, str] = config["board"]

    api_key = auth_opts["api_key"]
    token = auth_opts["token"]

    board_id = board_opts["board_id"]
    triage_list_id = board_opts["triage_list_id"]
    backlog_list_id = board_opts["backlog_list_id"]
