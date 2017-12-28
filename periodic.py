from commands.channel_report import channel_report
from config import *
from slacker import Slacker
from dispatch import dispatch

slacker = Slacker(SLACK_TOKEN)


if __name__ == "__main__":
    for (channel_name, channel_type) in channels_config:
        items = channel_report(channel_name, channel_type)
        if items:
            dispatch(items, channel_name, channel_type)