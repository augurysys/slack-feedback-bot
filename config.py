import os
from datetime import timedelta

channels_config = [
    ("code-reviews", "pr"),
    ("design-reviews", "doc"),
    ("spec-reviews-hack", "doc")

]

staleness_text = "It's lonely out here for *{name}*, if only someone would comment about {url}"
hype_text = "The party has already started, *{names}* are already there!, join with your comments! {url}"
hot_comment_text = "*{name}* dropped a bomb *{comment}* in {title}, what are you waiting for join the party? {url}"

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

MY_BOT_ID = "U8KKHE011"

MESSAGES_LIMIT = 100

COMMAND_PREFIX = "%"

STALENESS_CRITERION = "staleness"
DOC_STALENESS_THRESHOLD = timedelta(days=2)
PR_STALENESS_THRESHOLD = timedelta(days=3)

HYPE_THRESHOLD = 3
HYPE_CRITERION = "hype"

BOT_MENTION_CRITERION = "bot_mention"
HOT_COMMENT_CRITERION = "hot_comment"
HOT_COMMENT_THRESHOLD = 3

