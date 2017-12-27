import os
from datetime import timedelta

channels_config = [
    ("code-review", "pr")
]

slack_token = os.getenv("SLACK_TOKEN")
github_token= os.getenv("GITHUB_TOKEN")

STALENESS_THRESHOLD = timedelta(days=2)
STALENESS_CRITERION = "staleness"

HYPE_THRESHOLD = 3
HYPE_CRITERION = "hype"