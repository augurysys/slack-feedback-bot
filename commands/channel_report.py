from itemizers import itemizer_factory
from slack_scrapper import SlackScrapper
from config import *
from criteria.verifier import Verifier
from config import SLACK_TOKEN


def chosen_item(items):

    def _criterion_compare(i1, i2, _type):

        if _type == STALENESS_CRITERION:
            return True
            # return i1[1]['delta'] > i2[1]['delta']
        
        if _type == HYPE_CRITERION:
            return i1[1]['unique_commenters'] > i2[1]['unique_commenters']

        if _type == HOT_COMMENT_CRITERION:
            return i1[1]['comment'].replies_count > i2[1]['comment'].replies_count

        return False

    def _item_compare(i1, i2):

        i1_t = i1[1]['type']
        i2_t = i2[1]['type']

        if i1_t == i2_t:
            return 1 if _criterion_compare(i1, i2, i1_t) else -1

        if i1_t == STALENESS_CRITERION:
            return 1

        if i1_t == HOT_COMMENT_CRITERION:
            if i2_t == STALENESS_CRITERION:
                return -1
            else:
                return 1
        
        if i1_t == HYPE_CRITERION:
            return -1


    return sorted(items, cmp=_item_compare, reverse=True)[0]    

def channel_report(channel_name, channel_type):
    itemizer = itemizer_factory(channel_type)
    scrapper = SlackScrapper(channel_name, SLACK_TOKEN)
    scrapper.parse(itemizer)
    itemizer.enrich()
    items = itemizer.items.values()

    critera_verifier = Verifier(channel_type)
    items = critera_verifier.verify(items)
    if items:
        return [chosen_item(items)]

    return None
