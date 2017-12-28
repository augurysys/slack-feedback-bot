import re

import itertools

from model.item import Item, Comment
from datetime import datetime


class DrItemizer():
    def __init__(self, drive_client):
        self.items = dict()
        self.drive_client = drive_client

    def parse_message(self, message):
        text = message.text

        dr_id = parse_dr_id(text)
        if not dr_id:
            return
        print dr_id

        if dr_id in self.items:
            item = self.items[dr_id]

            if item.first_mentioned > message.timestamp:
                item.first_mentioned = message.timestamp

            if item.last_mentioned < message.timestamp:
                item.last_mentioned = message.timestamp

            if message.is_bot and (item.last_mentioned_bot is None or item.last_mentioned_bot < message.timestamp):
                item.last_mentioned_bot = message.timestamp
        else:
            item = Item()
            item.id = dr_id
            item.type = 'dr'
            item.first_mentioned = message.timestamp
            item.last_mentioned = message.timestamp
            if message.is_bot:
                item.last_mentioned_bot = message.timestamp
            self.items[dr_id] = item

    def enrich(self):

        for key, item in self.items.iteritems():
            dr = self.drive_client.files().get(fileId=item.id, fields="owners, name").execute()

            owner_name = dr['owners'][0]['displayName']
            item.owner = dr['owners'][0]['emailAddress']
            item.title = dr['name']

            dr_comments = self.drive_client.comments().list(fileId=item.id, fields="comments").execute()['comments']

            for comment in dr_comments:
                all_replies = list(comment['replies'])
                all_replies.insert(0, comment)
                for reply in all_replies:

                    if owner_name == reply['author']['displayName'] or reply['deleted'] or not reply.get('content'):
                        continue
                    com = Comment()
                    com.time = reply['createdTime']
                    com.time = datetime.strptime(com.time, '%Y-%m-%dT%H:%M:%S.%fZ')
                    com.owner = reply['author']['displayName']
                    com.text = reply['content']
                    item.comments.append(com)


def parse_dr_id(text):
    res = re.search('<https://docs.google(.*?)>', text)
    if not res:
        return None

    res = re.search('/[-\w]{25,}/', res.group())
    if not res:
        return None

    file_id = res.group().replace("/", "")
    return file_id
