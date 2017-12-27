import os

channels_config = [
    ("code-reviews", "pr")
]

slack_token = os.getenv("SLACK_TOKEN")
github_token= os.getenv("GITHUB_TOKEN")