from argparse import ArgumentParser
from datetime import datetime
from notion_client import getDailyLogId, getDailyLogContentBlocks
from executor import executeSlackPost

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-D', '--date', type=str, help='Date of the Log')
    args = parser.parse_args()

    if args.date:
        date = datetime(year=int(args.date[:5]), month=int(args.date[5:7]), day=int(args.date[7:]))

    try:
        page_id = getDailyLogId(date)
        blocks = getDailyLogContentBlocks(page_id)
        executeSlackPost(blocks)
        print(f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S+0900')} Success")
    except Exception as e:
        print(f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S+0900')} Error: {e}")
