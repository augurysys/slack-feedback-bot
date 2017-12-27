from datetime import datetime
from config import *


class Criterion(object):

    def __init__(self, item_type):
        pass

    def test(self, item):
        raise NotImplementedError


def Staleness(Criterion):

    def __init__(self, item_type):
        self._now = datetime.now()

    def test(self, item):        
        comment_times = [c.time for c in item.comments]
        comment_times.sort(reverse=True)

        if not comment_times:
            comment_delta = (self._now - item.last_mention)
            commented = False
        else:
            comment_delta = (comment_times[0] - item.last_mention)
            commented = True

        if comment_delta > STALENESS_THRESHOLD:
            item.tests[STALENESS_CRITERION] = {
                    "delta": comment_delta,
                    "commented": commented
                }

        return

def Hype(Criterion):

    def __init__(self, item_type):
        pass

    def test(self, item):
        unique_commenters = set([c.owner for c in item.comments])

        if unique_commenters >= HYPE_THRESHOLD:
            item.tests[HYPE_CRITERION] = {
                    "unique_commenters": unique_commenters
                }

def Ignored(Criterion):

    def __init__(self, item_type):
        pass

    def test(self, item):
        unique_commenters = set([c.owner for c in item.comments])

        if unique_commenters < IGNORE_THRESHOLD:
            item.tests[IGNORE_CRITERION] = {
                    "unique_commenters": unique_commenters
                }
