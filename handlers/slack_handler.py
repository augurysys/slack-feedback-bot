import traceback

from slackclient import SlackClient
import time
from slacker import Slacker
import config


class SlackHandler(object):
    def __init__(self):
        self.slacker = Slacker(config.SLACK_TOKEN)

    def init(self):
        sc = SlackClient(config.SLACK_TOKEN)
        slacker = Slacker(config.SLACK_TOKEN)

        if sc.rtm_connect():
            while True:
                try:
                    messages = sc.rtm_read()
                    for message in messages:

                        print "Incoming message.. {}".format(message)

                        if message.get("type", "") != "message":
                            continue

                        print "Handling message.. {}".format(message.get("text", ""))
                except Exception as e:
                    e_str = traceback.format_exc()
                    print str(e)
                    print str(e_str)
                    time.sleep(5)
                    print "trying to renew connection with slack..."
                    is_connected = sc.rtm_connect()
                    print "is connected:[{}]".format(is_connected)
        else:
            raise RuntimeError("Connection failed, invalid token?")

    @staticmethod
    def is_command(text):
        return len(text) > 1 and text[0] == config.COMMAND_PREFIX

    def route(self, text):
        if not SlackHandler.is_command(text):
            return






