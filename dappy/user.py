class User(object):
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __call__(self):
        pass

    def __str__(self):
        return f"Id: {self.id} | Title: {self.title}"
