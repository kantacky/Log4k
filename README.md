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

## cron.d/cron_file
```
chmod 755 ./cron.d/cron_file
```

## Execute
```
python -m log4k
```

If you would like to specify the date (Example: July 1st, 2023):
```
python -m log4k -D 20230701
```

&copy; 2023 Kanta Oikawa
