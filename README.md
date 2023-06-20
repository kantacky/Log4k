# Log4k Post App
## .env
- CONFIG_FILE_PATH
- NOTION_INTERNAL_INTEGRATION_TOKEN
- NOTION_LOG4K_DATABASE_ID

## .config.yml
```
services:
    slack:
        workspace_name:
            user_oauth_token: user_oauth_token
            signing_secret: signing_secret
            channels:
                channel_name: channel_id
```

&copy; 2023 Kanta Oikawa
