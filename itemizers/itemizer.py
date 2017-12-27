from .pr_itemizer import PrItemizer
from .dr_itemizer import DrItemizer
from github import Github
from config import GITHUB_TOKEN
import httplib2
import apiclient.http
from oauth2client.service_account import ServiceAccountCredentials

github_client = Github(login_or_token=GITHUB_TOKEN)

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    './augury-bi-868deec84c0a.json',
    ['https://www.googleapis.com/auth/drive',
     'https://www.googleapis.com/auth/drive.file']).create_delegated('amizrachi@augury.com')

http = httplib2.Http()
credentials.authorize(http)
drive_service = apiclient.discovery.build('drive', 'v3', http=http)


def itemizer_factory(itemizer_type):
    if itemizer_type == 'pr':
        return PrItemizer(github_client)
    elif itemizer_type == 'dr':
        return DrItemizer(drive_service)
