import os

channels_config = [
    {"code-review", "pr"}
]

slack_token = os.getenv("SLACK_TOKEN")

def get_channels_config():
    return channels_config

def get_slack_token():
    return slack_token