from datetime import datetime
from config import *


class Criterion(object):
    def __init__(self, item_type):
        pass

    def test(self, item):
        raise NotImplementedError


class Staleness(Criterion):
    def __init__(self, item_type):
        self._now = datetime.now()

        if item_type == "doc":
            self._threshold = timedelta(days=2)
        elif item_type == "pr":
            self._threshold = timedelta(days=1)

    def test(self, item):
        comment_times = [c.time for c in item.comments]
        comment_times.sort(reverse=True)

        if not comment_times:
            comment_delta = (self._now - item.last_mentioned)
            commented = False
        else:
            comment_delta = (comment_times[0] - item.last_mentioned)
            commented = True

        if comment_delta > self._threshold:
            item.tests[STALENESS_CRITERION] = {
                "type": STALENESS_CRITERION,
                "delta": comment_delta,
                "commented": commented
            }

        return


class Hype(Criterion):
    def test(self, item):
        unique_commenters = set([c.owner for c in item.comments])

        if len(unique_commenters) >= HYPE_THRESHOLD:
            item.tests[HYPE_CRITERION] = {
                "type": HYPE_CRITERION,
                "unique_commenters": unique_commenters
            }


class BotMention(Criterion):
    def test(self, item):
        if item.last_mentioned_bot:
            item.tests[BOT_MENTION_CRITERION] = {"type": BOT_MENTION_CRITERION,
                                                 "last_mentioned_bot": item.last_mentioned_bot}

class HotComment(Criterion):
    def test(self, item):

        if item.comments:
            sorted_comments = sorted(item.comments, key=lambda i: i.replies_count, reverse=True)

            item.tests[HOT_COMMENT_CRITERION] = {"type": HOT_COMMENT_CRITERION, "comment": sorted_comments[0]}

