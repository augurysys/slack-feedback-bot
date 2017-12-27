import os
from datetime import timedelta

channels_config = [
    ("code-reviews", "pr"),
    ("design-reviews", "dr")
]

slack_token = os.getenv("SLACK_TOKEN")
github_token= os.getenv("GITHUB_TOKEN")

MY_BOT_ID = "U8KKHE011"

STALENESS_THRESHOLD = timedelta(days=2)
STALENESS_CRITERION = "staleness"

HYPE_THRESHOLD = 3
HYPE_CRITERION = "hype"

IGNORE_THRESHOLD = 1
IGNORE_CRITERION = "ignore"