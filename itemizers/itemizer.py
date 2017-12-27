from .pr_itemizer import PrItemizer
from .dr_itemizer import DrItemizer


def itemizer_factory(itemizer_type):
    if itemizer_type == 'pr':
        return PrItemizer()
    elif itemizer_type == 'dr':
        return DrItemizer()
