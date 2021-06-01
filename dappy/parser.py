import collections
import csv
from warnings import showwarning
from bs4 import BeautifulSoup
from user import *


class Dappy(object):
    def __init__(self, _html):
        self.users = collections.defaultdict(list)
        self.html = open(_html)
        self.soup = BeautifulSoup(self.html, "html.parser")

    def __call__(self):
        pass

    def get_all_users(self):
        message_headers = self.soup.find_all("span", {"class": "chatlog__author-name"})
        for header in message_headers:
            user = get_user_from_message_header(header)
            self.users[user.id].append(user.title)
        self.users = get_user_list_from_dict(self.users)
        self.show_all_users()

    def show_all_users(self):
        print(user for user in self.users)


if __name__ == "__main__":
    dappy = Dappy("frostbite.html")
    dappy.get_all_users()