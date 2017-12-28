from itemizers import itemizer_factory
from slack_scrapper import SlackScrapper
from config import SLACK_TOKEN

def list(channel_name, channel_type, project):
    itemizer = itemizer_factory(channel_type)
    scrapper = SlackScrapper(channel_name, SLACK_TOKEN)
    scrapper.parse(itemizer)
    itemizer.enrich()
    items = itemizer.items.values()
    if project:
        items = list(filter(lambda item: item == project, items))
    return items
