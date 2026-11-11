import json
import os
import urllib.request
import urllib.error

token = os.environ["WEBEX_BOT_TOKEN"]
room_id = os.environ["WEBEX_ROOM_ID"]
status = os.environ.get("JENKINS_BUILD_STATUS", "UNKNOWN")
job = os.environ.get("JOB_NAME", "python-ci-webex")
build = os.environ.get("BUILD_NUMBER", "Unknown")

message = (
    f"**Jenkins Build: {status}**\n\n"
    f"**Project:** {job}\n\n"
    f"**Build:** #{build}\n\n"
    f"**Status:** {status}"
)

payload = json.dumps({
    "roomId": room_id,
    "markdown": message
}).encode("utf-8")

request = urllib.request.Request(
    "https://webexapis.com/v1/messages",
    data=payload,
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(request, timeout=20) as response:
        print(f"Webex notification sent: HTTP {response.status}")
except urllib.error.HTTPError as error:
    print(f"Webex notification failed: HTTP {error.code}")
    raise SystemExit(1)
except urllib.error.URLError:
    print("Webex notification failed: Connection error")
    raise SystemExit(1)