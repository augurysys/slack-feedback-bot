import re
import Slacker

class SlackScrapper:
    def __init__(self, channel_name, slack_token):
        self.slacker = Slacker(slack_token)
        self.channel_id = self.slacker.channels.get_channel_id(channel_name)


    def parse(self, itemizer):
        messages = self.slacker.channels.history(self.channel_id)
        for message in messages.body["messages"]:
            itemizer.parse_message(message)