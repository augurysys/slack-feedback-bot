from commands.channel_report import channel_report
from config import *
from slacker import Slacker

slacker = Slacker(SLACK_TOKEN)


def dispatch(items, channel, channel_type):

    item_strs = []
    for item in items:
        item_strs.append("{} ({}): {}".format(item[0].title, item[0].owner, item[1]['type']))
    lines = "\n".join(item_strs)
    msg = "******** {} FEEDBACK BOT RESPONSE **********\n{}".format(channel_type, lines)
    print item_strs
    slacker.chat.post_message(channel, text=msg)


if __name__ == "__main__":
    for (channel_name, channel_type) in channels_config:
        items = channel_report(channel_name, channel_type)
        if items:
            dispatch(items, channel_name, channel_type)