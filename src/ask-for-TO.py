import os
import slack
import subprocess
from datetime import datetime, timedelta

# 1 Ask for any TO?
client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'], ssl=False)

time_now = str(subprocess.check_output(["date", "+%H"]), 'utf-8') # bytes returned here contains a '\n'
print(time_now.rstrip('\n'))

if(time_now.rstrip('\n') == '12'):
    SLACK_USERGROUP = os.environ['SLACK_EAST_USERGROUP']

if(time_now.rstrip('\n') == '16'):
    SLACK_USERGROUP = os.environ['SLACK_WEST_USERGROUP']

response = client.chat_postMessage(channel=os.environ['CHANNEL_ID'], text=":minion_yah: Hi "+SLACK_USERGROUP+ " Any TO? Please update the tool with your TO case: https://commit.cfapps.io/turnover and begin reaching out to your pair :blob_council:")
