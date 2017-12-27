from commands.channel_report import channel_report
from config import *


if __name__ == "__main__":
    for (channel_name, channel_type) in channels_config:
        channel_report(channel_name, channel_type)