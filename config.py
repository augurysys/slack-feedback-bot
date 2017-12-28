import os
from datetime import timedelta

channels_config = [
    ("code-reviews-hack", "pr"),
    ("design-reviews", "doc"),
    ("specs-reviews", "doc")

]

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
GITHUB_TOKEN= os.getenv("GITHUB_TOKEN")

MY_BOT_ID = "U8KKHE011"

MESSAGES_LIMIT = 50

COMMAND_PREFIX = "%"

STALENESS_CRITERION = "staleness"

HYPE_THRESHOLD = 3
HYPE_CRITERION = "hype"

BOT_MENTION_CRITERION = "bot_mention"