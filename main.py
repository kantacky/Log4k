import config
from datetime import datetime
from notion_client import getDailyLogId, getDailyLogContentBlocks
from slack_client import convertToSlackBlocks, postToSlackChannel

def executeSlackPost(blocks):
    content = convertToSlackBlocks(blocks)
    slack_config = config.getConfig('slack')
    for properties in slack_config.values():
        user_oauth_token = properties['user_oauth_token']
        signing_secret = properties['signing_secret']
        for channel_id in properties['channels'].values():
            postToSlackChannel(user_oauth_token, signing_secret, channel_id, content)

if __name__ == '__main__':
    try:
        page_id = getDailyLogId()
        blocks = getDailyLogContentBlocks(page_id)
        executeSlackPost(blocks)
        print(f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S+0900')} Success")
    except Exception as e:
        print(f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S+0900')} Error: {e}")
