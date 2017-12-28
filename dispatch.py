from slacker import Slacker
from config import *

slacker = Slacker(SLACK_TOKEN)


def _format(item):

    item_type = item[1]['type']
    text = ""

    if item_type == STALENESS_CRITERION:
        text = staleness_text.format(name=item[0].owner, url=item[0].url)
    elif item_type == HYPE_CRITERION:
        users = list(set(c.owner for c in item[0].comments))
        text = hype_text.format(names=", ".join(users), url=item[0].url)
    elif item_type == HOT_COMMENT_CRITERION:
        commenter = item[1]['comment'].owner
        comment_text = item[1]['comment'].text

        text= hot_comment_text.format(name=commenter, text=comment_text, title=item[0].title, url=item[0].url)
    else:
        return None
    
    return {
        "fields": [{
            "value": text
        }]
    }

def dispatch(items, channel, _type):

    attachments = []
    for item in items:
        _f = _format(item)
        if _f:
            attachments.append(_f)
    
    print attachments
    slacker.chat.post_message(channel, attachments=attachments, as_user=True) 