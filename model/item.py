class Comment(object):
    def __init__(self):
        self.owner = None
        self.text = None
        self.time = None
        self.replies_count = 0


class Item(object):
    def __init__(self):
        self.id = None
        self.type = None
        self.owner = None
        self.title = None
        self.last_mentioned_bot = None
        self.first_mentioned = None
        self.last_mentioned = None
        self.comments = []
        self.tests = {}
        self.url = None
        self.project = None
