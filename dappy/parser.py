import collections
import csv
from bs4 import BeautifulSoup
from user import User


class Dappy(object):
    def __init__(self, _html):
        self.users = collections.defaultdict(list)
        self.html = open(_html)
        self.soup = BeautifulSoup(self.html, "html.parser")

    def __call__(self):
        pass


if __name__ == "__main__":
    dappy = Dappy("frostbite.html")