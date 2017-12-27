

class Verifier(object):

    def __init__(self, item_type):
        self._init_criteria(item_type)

    def _init_criteria(self, item_type):
        self._criteria = [
            Staleness(item_type),
            Hype(item_type),            
        ]

    def verify(self, items):
        for item in items:
            for criterion in self._criteria:
                criterion.test(item)

        return [item for item in items if item.tests]

            
