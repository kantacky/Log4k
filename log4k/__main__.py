from argparse import ArgumentParser
from datetime import datetime
from log4k.notion_client import getDailyLogId, getDailyLogContentBlocks
from log4k.executor import executeSlackPost

if __name__ == '__main__':
    try:
        parser = ArgumentParser()
        parser.add_argument('-D', '--date', type=str, help='Date of the Log')
        args = parser.parse_args()

        if args.date:
            date = datetime(year=int(args.date[:4]), month=int(args.date[4:6]), day=int(args.date[6:]))
            page_id = getDailyLogId(date)
        else:
            page_id = getDailyLogId()

        blocks = getDailyLogContentBlocks(page_id)

        if date:
            executeSlackPost(blocks, date)
        else:
            executeSlackPost(blocks)

        print(f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S+0900')} Success")

    except Exception as e:
        print(f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S+0900')} Error: {e}")
