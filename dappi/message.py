from bs4 import BeautifulSoup
from . import all


class Message(object):
    def __init__(self, user, message, timestamp):
        self.user = user
        self.message = message
        self.timestamp = timestamp

    def __call__(self):
        pass

    def __str__(self):
        return f"@{self.timestamp} - User: {self.user.title}: {self.message}"


def show_all_messages(messages):
    for message in messages:
        print(message)


def get_all_messages(soup):
    messages = []
    message_divs = soup.find_all("div", {"class": "chatlog__message-group"})
    for message_div in message_divs:
        user = get_user_from_message_div(message_div)
        message = get_message_from_message_div(user, message_div)
        messages.append(message)
    return messages


def get_message_from_message_div(user, message_div):
    message = message_div.find("span", {"class": "markdown"}).text
    timestamp = get_date_time_from_string(
        message_div.find("span", {"class": "chatlog__timestamp"}).text
    )
    return Message(user, message, timestamp)


def get_messages_by_user_id(messages, user_id):
    for message in messages:
        pass