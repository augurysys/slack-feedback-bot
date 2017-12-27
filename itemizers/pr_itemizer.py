from github import Github
import config
class PrItemizer(object):

    def __init__(self):
        self.items = {}


    def parse_message(self, message):
        pass

    def enrich(self):

        for item in self.items:
            
            self.github_client = Github(login_or_token=config.github_token)
            self.github_client.get_repo(self.item.repo).get_pull(item.pull_number)














