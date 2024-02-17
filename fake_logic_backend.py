import random
user = ""
fake_player_db = ["player 1", "player 2", "player 3", "player 4", "player 5", "player 6", "player 7"]


def login(username, password):
    if username == "a" and password == "a":
        global user
        user = username
        return True
    else:
        return False


def get_high_score():
    return "10"


def get_user_name():
    return user


def get_fake_random_player():
    return fake_player_db[random.randint(1, len(fake_player_db) - 1)]


def get_fake_search_player(name):
    if name in fake_player_db:
        return f"Successfully found player {name}"
    else:
        return f"no player like {name}"

