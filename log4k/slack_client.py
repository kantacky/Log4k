from datetime import datetime
from slack_bolt import App

def convertToSlackBlocks(blocks, date: datetime = datetime.today()):
    slack_blocks = []

    slack_blocks.append({
        'type': 'header',
        'text': {
            'type': 'plain_text',
            'text': date.strftime('%Y-%m-%d'),
        }
    })

    content = ''

    for block in blocks:
        block_type = block['type']
        rich_text = block[block_type]['rich_text']
        if len(rich_text) > 0:
            if block_type == 'heading_1' or block_type == 'heading_2' or block_type == 'heading_3':
                if content != '':
                    slack_blocks.append({
                        'type': 'section',
                        'text': {
                            'type': 'mrkdwn',
                            'text': content,
                        }
                    })

                    content = ''

                content += f"*{rich_text[0]['plain_text']}*\n"

            elif block_type == 'paragraph':
                for item in rich_text:
                    if item['text']['link'] is None:
                        content += f"{item['text']['content']}"
                    else:
                        content += f"<{item['text']['link']['url']}|{item['text']['content']}>"

                content += '\n'

            elif block_type == 'bulleted_list_item':
                content += f"• "
                for item in rich_text:
                    if item['text']['link'] is None:
                        content += f"{item['text']['content']}"
                    else:
                        content += f"<{item['text']['link']['url']}|{item['text']['content']}>"

                content += '\n'

    if content != '':
        slack_blocks.append({
            'type': 'section',
            'text': {
                'type': 'mrkdwn',
                'text': content,
            }
        })

    slack_blocks.append({
        'type': 'context',
        'elements': [
            {
                "type": "image",
                "image_url": "https://www.kantacky.com/content/images/2023/04/IconTransparent1200.png",
                "alt_text": "Log4k"
            },
            {
                'type': 'plain_text',
                'text': 'This message was sent by Log4k automatically.',
            }
        ]
    })

    return slack_blocks

def postToSlackChannel(user_oauth_token, signing_secret, channel_id, content):
    app = App(token=user_oauth_token, signing_secret=signing_secret)

    app.client.chat_postMessage(
        channel=channel_id,
        text='Log4k',
        blocks=content,
    )
