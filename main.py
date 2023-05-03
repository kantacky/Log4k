import asyncio
import config
from datetime import datetime
from discord_client import postToDiscordChannel
from notion_client import getDailyLogId, getDailyLogContentBlocks
from slack_client import convertToSlackBlocks, postToSlackChannel

def executeDiscordPost(blocks):
    loop = asyncio.get_event_loop()
    try:
        discord_config = config.getConfig('discord')
        for properties in discord_config.values():
            token = properties['token']
            for channel_id in properties['channels'].values():
                loop.run_until_complete(postToDiscordChannel(token, channel_id, str(blocks)))
        print(f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S+0900')} Success: Discord Post")
    except Exception as e:
        print(f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S+0900')} Error: {e}")            

def executeSlackPost(blocks):
    try:
        content = convertToSlackBlocks(blocks)
        slack_config = config.getConfig('slack')
        for properties in slack_config.values():
            user_oauth_token = properties['user_oauth_token']
            signing_secret = properties['signing_secret']
            for channel_id in properties['channels'].values():
                postToSlackChannel(user_oauth_token, signing_secret, channel_id, content)
        print(f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S+0900')} Success")
    except Exception as e:
        print(f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S+0900')} Error: {e}")

if __name__ == '__main__':
    try:
        page_id = getDailyLogId()
        blocks = getDailyLogContentBlocks(page_id)
        # executeDiscordPost(blocks)
        executeSlackPost(blocks)
        print(f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S+0900')} Success")
    except Exception as e:
        print(f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S+0900')} Error: {e}")
