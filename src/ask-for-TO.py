import os
import slack
import subprocess
import csv
from datetime import datetime, timedelta

# 1 Ask for any TO?
client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'], ssl=False)

response = client.chat_postMessage(channel=os.environ['CHANNEL_ID'], text=":minion_yah: Hi "+os.environ['SLACK_EAST_USERGROUP']+ " Any TO? Please update the tool with your TO case: https://commit.cfapps.io/turnover and add TO notes to the case. :minion_yah:")
