import os
from datetime import timedelta

channels_config = [
    ("code-reviews-hack", "pr"),
    ("design-reviews-hack", "doc"),
    ("spec-reviews-hack", "doc")

]

staleness_text = "It's lonely out here for {name}, if only someone would comment about {url}\n https://giphy.com/gifs/season-20-the-simpsons-20x4-3orieMT2LQqzUXrnxe"
hype_text = "The party has already started, {names} are already there!, join with your comments! {url}\n https://giphy.com/gifs/koksalbaba-party-break-dance-xT9IgfraGfHU8t1p5u"
hot_comment_text = "{name} dropped a bomb *{comment}* in {title}, what are you waiting for join the party? {url}\n https://giphy.com/gifs/animation-explosion-bomb-FnatKdwxRxpVC"

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

MY_BOT_ID = "U8KKHE011"

MESSAGES_LIMIT = 100

COMMAND_PREFIX = "%"

STALENESS_CRITERION = "staleness"

HYPE_THRESHOLD = 3
HYPE_CRITERION = "hype"

BOT_MENTION_CRITERION = "bot_mention"
HOT_COMMENT_CRITERION = "hot_comment"

