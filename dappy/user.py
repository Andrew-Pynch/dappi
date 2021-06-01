from bs4 import BeautifulSoup


class User(object):
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __call__(self):
        pass

    def __str__(self):
        return f"Id: {self.id} | Title: {self.title}"


def get_user_from_message_header(message_header):
    id = message_header["data-user-id"]
    title = message_header["title"]
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
