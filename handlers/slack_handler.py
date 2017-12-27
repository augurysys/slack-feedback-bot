from slacker import Slacker

import config


class Slack_handler(object):
    def __init__(self):
        self.slacker = Slacker(config.slack_token)

    def init(self):
        self.slacker.rtm.start()
        res = self.slacker.rtm.connect()
        print "res {}".format(res)

        while True:
            self.slacker.rtm










