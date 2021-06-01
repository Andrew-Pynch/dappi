import collections
import csv
from warnings import showwarning
from bs4 import BeautifulSoup
from user import *
from message import *


class Parser(object):
    def __init__(self, html, output_dir, show):
        self.user_dict = collections.defaultdict(list)
        self.users = []
        self.messages = []
        self.html = open(html)
        self.output_dir = output_dir
        self.show = show
        self.soup = BeautifulSoup(self.html, "html.parser")
        self.populate_users()
        self.populate_messages()

    def __call__(self):
        pass

    def populate_users(self):
        self.user_dict, self.users = get_all_users(
            self.soup, self.user_dict, self.users
        )

    def populate_messages(self):
        self.messages = get_all_messages(self.soup)

    def parse_all_messages_into_single_file(self):
        with open(self.output_dir, "w", newline="") as f:
            field_names = ["id", "title", "message", "timestamp"]

            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()

            for message in self.messages:
                self.show and print(message) # Print message if show is true 
                writer.writerow(
                    {
                        "id": message.user.id,
                        "title": message.user.title,
                        "message": message.message,
                        "timestamp": message.timestamp,
                    }
                )


# if __name__ == "__main__":
#     dappy = Parser("frostbite.html")
#     dappy.parse_all_messages_into_single_file()