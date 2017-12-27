import os
from datetime import timedelta

channels_config = [
    ("code-reviews", "pr"),
    ("design-reviews", "dr")
]

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
GITHUB_TOKEN= os.getenv("GITHUB_TOKEN")

MY_BOT_ID = "U8KKHE011"

COMMAND_PREFIX = "%"

STALENESS_THRESHOLD = timedelta(days=2)
STALENESS_CRITERION = "staleness"

HYPE_THRESHOLD = 3
HYPE_CRITERION = "hype"

IGNORE_THRESHOLD = 1
IGNORE_CRITERION = "ignore"