#!/bin/bash

# Requires credhub login prior to execution

credhub set -n /concourse/main/tobot/TZ -t value -v "America/Los_Angeles"
credhub set -n /concourse/main/tobot/CHANNEL_ID -t value -v ""
credhub set -n /concourse/main/tobot/SLACK_API_TOKEN -t value -v ""
credhub set -n /concourse/main/tobot/GOOGLE_SHEET_URL -t value -v ""
credhub set -n /concourse/main/tobot/COMMITS_LINK -t value -v ""
credhub set -n /concourse/main/tobot/SLACK_EAST_USERGROUP -t value -v ''
credhub set -n /concourse/main/tobot/SLACK_WEST_USERGROUP -t value -v ''
credhub set -n /concourse/main/tobot/SLACK_EMEA_USERGROUP -t value -v ''
credhub set -n /concourse/main/tobot/SLACK_APJ_USERGROUP -t value -v ''
