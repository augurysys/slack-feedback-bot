from config import STALENESS_THRESHOLD, STALENESS_CRITERION


class Criterion(object):

    def __init__(self, item_type):
        pass

    def test(self, item):
        raise NotImplementedError

    def approve(self, item):
        raise NotImplementedError


def Staleness(Criterion):

    def __init__(self, item_type):
        self._now = datetime.now()

    def test(self, item):        
        comment_times = [c.time for c in item.comments]
        comment_times.sort(reverse=True)

        if not comment_times:
            comment_delta = (now - item.last_mention)
            commented = False
        else:
            comment_delta = (comment_times[0] - item.last_mention)
            commented = True

        if comment_delta > STALENESS_THRESHOLD:
            item.tests.append({
                "type": STALENESS_CRITERION,
                "data": {
                    "delta": comment_delta,
                    "commented": commented
                }
            })

        return

def Hype(Criterion):

    def __init__(self, item_type):
        pass

    def test(self, item):

        unique_commenters = set([c.owner for c in item.comments])

        if unique_commenters >= HYPE_THRESHOLD:
            item.tests.append({
                "type": HYPE_CRITERION,
                "data": {
                    "unique_commenters": unique_commenters
                }
            })
