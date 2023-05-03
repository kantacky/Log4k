from dotenv import load_dotenv
import os
import yaml

load_dotenv()

NOTION_INTERNAL_INTEGRATION_TOKEN = os.getenv('NOTION_INTERNAL_INTEGRATION_TOKEN')
NOTION_LOG4K_DATABASE_ID = os.getenv('NOTION_LOG4K_DATABASE_ID')

def getConfig(service):
    with open(os.getenv('CONFIG_FILE_PATH')) as f:
        config = yaml.safe_load(f)['services'][service]
        return config
