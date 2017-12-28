onfrom criteria import Staleness, Hype, BotMention, HotComment
from config import *


class Verifier(object):
    def __init__(self, item_type):
        self._init_criteria(item_type)

    def _init_criteria(self, item_type):
        
        _default_criteria = [
            BotMention(item_type),
            Staleness(item_type),
            Hype(item_type),
        ]

        if item_type == "doc":
            _default_criteria.append(HotComment(item_type))

        self._criteria = _default_criteria

    def verify(self, items):
        for item in items:
            for criterion in self._criteria:
                criterion.test(item)

        res = [(item, self._choose_criterion(item)) for item in items if item.tests]
        return [tup for tup in res if tup[1]]

    @staticmethod
    def _choose_criterion(item):

        criteria_keys = item.tests.keys()
        # if BOT_MENTION_CRITERION in criteria_keys:
        #     return None

        if STALENESS_CRITERION in criteria_keys:
            return item.tests[STALENESS_CRITERION]

        if HOT_COMMENT_CRITERION in criteria_keys:
            return item.tests[HOT_COMMENT_CRITERION]

        if HYPE_CRITERION in criteria_keys:
            return item.tests[HYPE_CRITERION]

        return None
