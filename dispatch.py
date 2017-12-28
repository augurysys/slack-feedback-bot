from slacker import Slacker
from config import *

slacker = Slacker(SLACK_TOKEN)


def _format(item):
    color = "good"if item[1]['type'] == HYPE_CRITERION else "danger"

    return {
        "color": color,
        "fields": [{
            "value": "{}: {}".format(item[0].owner, item[1]['type'])
        }]
    }

def dispatch(items):

    attachments = []
    for item in items:
        attachments.append(_format(item))
    
    channel = "#code-reviews-hack"
    print attachments
    slacker.chat.post_message(channel, attachments=attachments) 