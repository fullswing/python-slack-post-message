"""
usage: python main.py [option]

-t --title     : slack message in the title [THIS IS REQUIRED]
-b --body      : slack message in the thread
-c --chanel    : slack channel
-e --emoji     : slack bot emoji
-n --name      : slack bot name
"""


import slack
import argparse
import sys


def send_message(**payload):
    response = slack_client.chat_postMessage(**payload)
    return response["ts"]


def main():
    payload = {
        "channel": args.channel,
        "icon_emoji": args.emoji,
        "username": args.name,
        "text": args.title,
    }

    thread_ts = send_message(**payload)

    if not args.body:
        return

    payload["thread_ts"] = thread_ts

    thread_msg = args.body
    for msg in thread_msg:
        payload["text"] = msg
        send_message(**payload)


if __name__ == "__main__":
    slack_token = "your-slack-token"
    slack_client = slack.WebClient(token=slack_token)

    parser = argparse.ArgumentParser(description="slack")

    parser.add_argument("-t", "--title", type=str, required=True)
    parser.add_argument("-b", "--body", nargs="+", type=str)
    parser.add_argument("-e", "--emoji", type=str)
    parser.add_argument("-n", "--name", type=str, required=True)
    parser.add_argument("-c", "--channel", type=str, required=True)

    args = parser.parse_args()

    main()
