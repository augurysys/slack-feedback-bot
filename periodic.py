from config import *
from itemizers.itemizer import itemizer_factory
from slack_scrapper import SlackScrapper

for (channel_name, channel_type) in channels_config():
    itemizer = itemizer_factory(channel_type)
    scrapper = SlackScrapper(channel_name, slack_token)
    scrapper.parse(itemizer)
    itemizer.enrich()
    items = itemizer.items