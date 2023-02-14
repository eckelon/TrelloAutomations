import tomli

api_key = None
token = None
board_id = None
triage_list_id = None

with open("config/env.toml", mode="rb") as fp:
    config = tomli.load(fp)
    auth = config["auth"]
    board = config["board"]

    api_key = auth["api_key"]
    token = auth["token"]

    board_id = board["board_id"]
    triage_list_id = board["triage_list_id"]
    backlog_list_id = board["backlog_list_id"]
