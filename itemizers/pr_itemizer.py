from model.item import Item
from model.item import Comment


class PrItemizer(object):
    def __init__(self, github_client):
        self.items = dict()
        self.github_client = github_client

    def parse_message(self, message):
        text = message["text"]

        pr_id = parse_pr_id(text)
        if not pr_id:
            return

        if pr_id in self.items:
            item = self.items[pr_id]

            if item.first_mentioned > message.timestamp:
                item.first_mentioned = message.timestamp

            if item.last_mentioned < message.timestamp:
                item.last_mentioned = message.timestamp

            if message.is_bot and (item.last_mentioned_bot is None or item.last_mentioned_bot < message.timestamp):
                item.last_mentioned_bot = message.timestamp
        else:
            item = Item()
            item.id = pr_id
            item.type = 'pr'
            item.first_mentioned = message.timestamp
            item.last_mentioned = message.timestamp
            if message.is_bot:
                item.last_mentioned_bot = message.timestamp
            self.items[pr_id] = item

    def enrich(self):
        to_delete = []

        for key, item in self.items:
            repo, pull_number = item.id.split('_')
            pull_request = self.github_client.get_repo(repo).get_pull(pull_number)

            if pull_request.state != 'open':
                to_delete.append(item.id)
                continue

            item.owner = pull_request.user.login
            item.title = pull_request.title

            comments = pull_request.get_comments()
            for comment in comments:
                if pull_request.user.login == comment.user.login:
                    continue

                com = Comment()
                com.time = comment.created_at
                com.owner = comment.user.login
                com.text = comment.body
                item.comments.append(com)

        for key in to_delete:
            self.items.pop(key)


def parse_pr_id(message):
    if 'https://github.com/augurysys' not in message:
        return None
    items = message.split('/')
    index = items.index('augurysys')
    return '{}_{}'.format(items[index + 1], items[index + 3])
