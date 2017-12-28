import traceback

from slackclient import SlackClient
import time
from slacker import Slacker
import config
from commands.channel_report import channel_report
from commands.list_items import list_items

class SlackHandler(object):
    def __init__(self):
        self.slacker = Slacker(config.SLACK_TOKEN)
        self.sc = SlackClient(config.SLACK_TOKEN)

    def init(self):

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
            "stats": self.handle_stats,
            "reset": self.handle_reset
        }.get(command, self.command_not_found_handler)
        if handler:
            handler(user, channel, command, text)

    def command_not_found_handler(self, user, channel, command, text):
        print "command={} not found".format(command)

    def handle_reset(self, user, channel, command, text):
        self.sc.rtm_send_message(channel, "Reseting bot data in channel...")
        res = self.slacker.channels.history(channel)
        counter = 0
        messages = res.body["messages"]
        for message in messages:
            try:
                if "user" in message and message["user"] == config.MY_BOT_ID:
                    self.slacker.chat.delete(channel, message["ts"])
                    counter += 1
            except:
                pass
        self.sc.rtm_send_message(channel, "Removed {} messages from channel. _So fresh and so clean_")

    def get_list(self, user, channel, command, text):
        print "command list"
        self.sc.rtm_send_message(channel, "Fetching list...")
        channel_name, channel_type = self.get_channel_info(channel)
        res = list_items(channel_name, channel_type, text.strip())
        lines = ["{} by {}".format(r.url, r.owner) for r in res]
        return_message = "******** FEEDBACK BOT RESPONSE **********\n{}".format("\n".join(lines))
        self.sc.rtm_send_message(channel, return_message)

    def handle_stats(self, user, channel, command, text):
        print "command stats"
        # self.sc.rtm_send_message(channel, "Fetching stats...")
        channel_name, channel_type = self.get_channel_info(channel)
        res = channel_report(channel_name, channel_type)
        lines = ["{} by {} - {}".format(r[0].id, r[0].owner, r[1]["type"]) for r in res]
        if not lines:
            lines = ["This is so boring... Nothing new here..."]
        return_message  ="******** FEEDBACK BOT RESPONSE **********\n{}".format("\n".join(lines))
        self.sc.rtm_send_message(channel, return_message)

    def get_channel_info(self, channel_id):
        channels = self.slacker.channels.list(True)
        for channel in channels.body["channels"]:
            if channel["id"] == channel_id:
                for cc in config.channels_config:
                    if cc[0] == channel["name"].encode('utf-8'):
                        return cc
        return ""


    @staticmethod
    def is_command(text):
        return len(text) > 1 and text[0] == config.COMMAND_PREFIX





