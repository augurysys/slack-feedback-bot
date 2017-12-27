from itemizers import itemizer_factory
from slack_scrapper import SlackScrapper
from criteria.verifier import Verifier
from config import SLACK_TOKEN

def channel_report(channel_name, channel_type):
    itemizer = itemizer_factory(channel_type)
    scrapper = SlackScrapper(channel_name, SLACK_TOKEN)
    scrapper.parse(itemizer)
    itemizer.enrich()
    items = itemizer.items.values()

    critera_verifier = Verifier(channel_type)
    items = critera_verifier.verify(items)
    print items