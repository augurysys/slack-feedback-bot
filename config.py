import os

channels_config = [
    {"code-review", "pr"}
]

slack_token = os.getenv("SLACK_TOKEN")
github_token = os.getenv("GITHUB_TOKEN")

def get_channels_config():
    return channels_config

