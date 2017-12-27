class Message(object):
    def __init__(self, is_bot, timestamp, text):
        self.is_bot = is_bot
        self.timestamp = timestamp
        self.text = text
