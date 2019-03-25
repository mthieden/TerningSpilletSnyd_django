import json
import requests


def create_game(dice, players, username, token):
    data = {
        "username": username,
        "terninger": dice,
        "token": token,
        "spillere": players,
    }
    return requests.post(
        "http://130.225.170.205:8080/REST_Terning_server/games",
        data=json.dumps(data))


def login(username, password):
    data = {"username": username, "password": password}
    r = requests.post(
        "http://130.225.170.205:8080/REST_Terning_server/login",
        data=json.dumps(data))

    r.raise_for_status()
    return r.json()["token"]

def game():
    return requests.get("http://130.225.170.205:8080/REST_Terning_server/games").json()

def close_game(port, username, token):
    {
        "token": token,
        "username": username,
        "port": port,
    }
    return requests.post(
        "http://130.225.170.205:8080/REST_Terning_server/closeGame",
        data=json.dumps(data))

def close_games(username, token):
    {"token": token, "username": username}
    r = requests.post(
        "http://130.225.170.205:8080/REST_Terning_server/closeAllGames",
        data=json.dumps(data))
    r.raise_for_status()
