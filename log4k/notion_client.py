import config
from datetime import datetime
import requests

def getDailyLogId(date: datetime = datetime.today()):
    url = f'https://api.notion.com/v1/databases/{config.NOTION_LOG4K_DATABASE_ID}/query'

    headers = {
        'Authorization': f'Bearer {config.NOTION_INTERNAL_INTEGRATION_TOKEN}',
        'Content-type': 'application/json',
        'Notion-Version': '2022-06-28',
    }

    data = {
        'filter': {
            'property': 'Date',
            'date': {
                'equals': date.strftime('%Y-%m-%d')
            }
        }
    }

    return requests.post(url, headers=headers, json=data).json()['results'][0]['id']


def getDailyLogContentBlocks(page_id):
    url = f'https://api.notion.com/v1/blocks/{page_id}/children'

    headers = {
        'Authorization': f'Bearer {config.NOTION_INTERNAL_INTEGRATION_TOKEN}',
        'Notion-Version': '2022-06-28',
    }

    return requests.get(url, headers=headers).json()['results']
