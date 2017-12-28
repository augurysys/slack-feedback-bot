from slacker import Slacker
from config import *

slacker = Slacker(SLACK_TOKEN)


def _format(item):

    item_type = item[1]['type']
    
    text = ""
    image = None

    if item_type == STALENESS_CRITERION:
        text = staleness_text.format(name=item[0].owner, url=item[0].url)
        image = "https://media.giphy.com/media/3oFzmtbkFIVT3zb6hi/giphy.gif"
    elif item_type == HYPE_CRITERION:
        users = list(set(c.owner for c in item[0].comments))
        text = hype_text.format(names=", ".join(users), url=item[0].url)
        image = "https://media.giphy.com/media/xULW8GA2epJ7O0AnEk/giphy.gif"
    elif item_type == HOT_COMMENT_CRITERION:
        commenter = item[1]['comment'].owner
        comment_text = item[1]['comment'].text

        text= hot_comment_text.format(name=commenter, text=comment_text, title=item[0].title, url=item[0].url)
        image = "https://media.giphy.com/media/3ohc16Cky5Mu9rZwT6/giphy.gif"
    else:
        return None
    
    return {
        "fields": [{
            "value": text,
        }],
        "image_url": image,
        "mrkdwn_in": ["fields", "text"]        
    }

def dispatch(items, channel, _type):

    attachments = []
    for item in items:
        _f = _format(item)
        if _f:
            attachments.append(_f)
    channel = "code-reviews-hell"
    print attachments
    slacker.chat.post_message(channel, attachments=attachments, as_user=True) 