import os
import slack
import subprocess
from datetime import datetime, timedelta

# 1 Ask for any TO?
client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'], ssl=False)

response = client.chat_postMessage(channel=os.environ['CHANNEL_ID'], text=":minion_yah: Hi "+SLACK_USERGROUP+ " Any TO? Please update the tool with your TO case: "+os.environ['COMMITS_LINK']+" and begin reaching out to your pair :blob_council:")
