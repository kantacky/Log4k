from datetime import datetime
from log4k import config
from log4k.slack_client import convertToSlackBlocks, postToSlackChannel

def executeSlackPost(blocks, date: datetime = datetime.today()):
    content = convertToSlackBlocks(blocks, date)
    slack_config = config.getConfig('slack')
    for properties in slack_config.values():
        user_oauth_token = properties['user_oauth_token']
        signing_secret = properties['signing_secret']
        for channel_id in properties['channels'].values():
            postToSlackChannel(user_oauth_token, signing_secret, channel_id, content)
