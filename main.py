import os
import slack
import subprocess
import csv
from datetime import datetime, timedelta
'''
How can you automate this script?

- Using Concourse
    - Git clone the following repo for your concourse container. This repo will have the main.py (this same file) for the concourse container to pull in: https://github.com/artful-gopher/c3po.git 
    - Concourse job is going to run this script on weekdays at 1:00 PM PST using its timeresource. (According to your use case you can change the timezone as per your team(s) requirements) - pipeline.yml
    - Define following environment variables as params in your concourse task
    Note: These environment variable names must not change.
        1. TZ - timezone
        2. CHANNEL_ID - the channel ID on slack where you want to post the reminder.
        3. SLACK_API_TOKEN - this is your Slack's app bot token.
        4. GOOGLE_SHEET_URL - this is where to going to pull in names based on Monday's date of the current week.
        5. SLACK_HANDLE - user or user group you want to send the reminder.
'''

day = str(subprocess.check_output(["date", "+%A"]), 'utf-8') # bytes returned here contains a '\n'

'''
If its neither Saturday nor Sunday:
    1. Get todays date in PST (todays_date)
    2. Get Monday's date of the current week (mondays_date)
    3. Get names of the TO pair from the csv for mondays_date obtained in step2
    4. Send the reminder with correct names
'''
# rstrip method strips away the trailing newline from 
if(day.rstrip('\n') != 'Sunday' or day.rstrip('\n' != 'Saturday')):
    # 1 todays_date
    todays_date = str(subprocess.check_output(["date", "+%Y-%m-%d"]), 'utf-8')
    print(todays_date)

    # 2 mondays_date 
    dt = datetime.strptime(todays_date.rstrip('\n'), "%Y-%m-%d")
    mondays_date = dt - timedelta(days=dt.weekday())
    print(mondays_date.strftime("%Y-%m-%d"))

    # 3 get name of the TO pair
    os.system("curl -s $GOOGLE_SHEET_URL > /tmp/tosheet.csv") # get csv data from google sheet

    
    with open('/tmp/tosheet.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if(row[0] == mondays_date.strftime("%Y-%m-%d")):
                name1 = row[1]
                name2 = row[2]
                print(name1+" & "+name2)
                # 4 send the reminder
                client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'], ssl=False)
                response1 = client.chat_postMessage(channel=os.environ['CHANNEL_ID'], text=":robot_face: Hi "+os.environ['SLACK_HANDLE']+ " Quick Reminder: This week\'s EC to WC TO pair is "+name1+" and "+name2+" :robot_face:")
