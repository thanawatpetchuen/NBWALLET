import requests
from datetime import datetime
import time
req = requests.get("https://us-central1-nbwallet-nb.cloudfunctions.net/checkTx?id=5901012620045&type=users")

req_j = req.json()

print(len(req_j))

def timestampsimp(times):
    stt = str(times)
    unix_timestamp  = int(stt[:-3])
    utc_time = time.gmtime(unix_timestamp)
    local_time = time.localtime(unix_timestamp)
    # print(time.strftime("%Y-%m-%d %H:%M:%S", local_time))

    return time.strftime("%Y-%m-%d %H:%M:%S", local_time)

for item in req_j:
    # print(req_j[item])
    print(req_j[item]["Name"], req_j[item]["amount"], timestampsimp(req_j[item]["time"]), req_j[item]["to"])

    # print(req_j[item]["amount"])
    # print(req_j[item]["time"])
    # print(req_j[item]["to"])
