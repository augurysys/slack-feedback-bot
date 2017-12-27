from slacker import Slacker
from model.message import Message

MY_BOT_ID = "U8KKHE011"

class SlackScrapper(object):
    def __init__(self, channel_name, slack_token):
        self.slacker = Slacker(slack_token)
        print "Init slack scrapper with channel {}".format([channel_name])
        self.channel_id = self.slacker.channels.get_channel_id(channel_name)

    def parse(self, itemizer):
        print "Fetch messages from channel {}".format([self.channel_id])
        response = self.slacker.channels.history(self.channel_id)
        messages = response.body["messages"]

        for message in messages:
            if "subtype" in message or message["type"] != "message":
                continue
            is_bot = MY_BOT_ID == message["user"]
            msg = Message(is_bot, message["ts"], message["text"])
            print msg
            itemizer.parse_message(msg)