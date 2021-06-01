from bs4 import BeautifulSoup
from .message import *
from .dates import *

class User(object):
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __call__(self):
        pass

    def __str__(self):
        return f"Id: {self.id} | Title: {self.title}"


def get_all_users(soup, user_dict, users):
    message_headers = soup.find_all("span", {"class": "chatlog__author-name"})
    for header in message_headers:
        user = get_user_from_message_header(header)
        user_dict[user.id].append(user.title)
    users = get_user_list_from_dict(user_dict)
    return user_dict, users


def show_all_users(users):
    for user in users:
        print(user)


def get_user_from_message_header(message_header):
    id = message_header["data-user-id"]
    title = message_header["title"]
    return User(id, title)


def get_user_from_message_div(message_div):
    id = message_div.select("span", {"class": "chatlog__author-name"})[0][
        "data-user-id"
    ]
    title = message_div.select("span", {"class": "chatlog__author-name"})[0]["title"]
    return User(id, title)


def is_unique_user(user, users):
    return any(search_user.id == user.id for search_user in users)


def get_user_list_from_dict(user_dict):
    users = []
    for id in user_dict:
        unique_titles = list(dict.fromkeys(user_dict[id]))
        user = User(id, unique_titles)
        users.append(user)
    return users
