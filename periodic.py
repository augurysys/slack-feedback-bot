from config import *
from itemizers.itemizer import itemizer_factory
from slack_scrapper import SlackScrapper

for (channel_name, channel_type) in get_channels_config():
    itemizer = itemizer_factory(channel_type)
    scrapper = SlackScrapper(channel_name, get_slack_token())
    scrapper.parse(itemizer)