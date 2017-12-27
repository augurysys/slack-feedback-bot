import traceback

from slackclient import SlackClient
import time
from slacker import Slacker
import config
from commands.channel_report import channel_report


class SlackHandler(object):
    def __init__(self):
        self.slacker = Slacker(config.SLACK_TOKEN)

    def init(self):
        self.sc = SlackClient(config.SLACK_TOKEN)
        slacker = Slacker(config.SLACK_TOKEN)

        if self.sc.rtm_connect():
            while True:
                try:
                    messages = self.sc.rtm_read()
                    for message in messages:

                        print "Incoming message.. {}".format(message)

                        if message.get("type", "") != "message":
                            continue

                        channel = message.get("channel", "")
                        text = message.get("text", "")
                        user = message.get("user", "")

                        print "Handling message.. {}".format(text)

                        self.route(user, channel, text)
                except Exception as e:
                    e_str = traceback.format_exc()
                    print str(e)
                    print str(e_str)
                    time.sleep(5)
                    print "trying to renew connection with slack..."
                    is_connected = self.sc.rtm_connect()
                    print "is connected:[{}]".format(is_connected)
        else:
            raise RuntimeError("Connection failed, invalid token?")

    def route(self, user, channel, text):

        if not SlackHandler.is_command(text):
            return

        command = text[1:].split(" ")[0]
        text = text[len(command)+1:]

        handler = {
            "list": self.get_list,
            "stats": self.handle_stats
        }.get(command, self.command_not_found_handler)
        if handler:
            handler(user, channel, command, text)

    def command_not_found_handler(self, user, channel, command, text):
        print "command={} not found".format(command)

    def get_list(self, user, channel, command, text):
        print "command list"

    def handle_stats(self, user, channel, command, text):
        print "command stats"
        channel_name, channel_type = self.get_channel_info(channel)
        res = channel_report(channel_name, channel_type)
        return_message  ="******** FEEDBACK BOT RESPONSE **********\n{}".format(res.join(", "))
        self.sc.rtm_send_message(channel, return_message)

    def get_channel_info(self, channel_id):
        channels = self.slacker.channels.list(True)
        for channel in channels.body["channels"]:
            if channel["id"] == channel_id:
                for cc in config.channels_config:
                    if cc[0] == channel["name"]:
                        return cc
        return ""


    @staticmethod
    def is_command(text):
        return len(text) > 1 and text[0] == config.COMMAND_PREFIX




