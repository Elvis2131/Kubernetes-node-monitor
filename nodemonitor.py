import requests
from threading import Timer
from slack import send_slack_message
import json,os,datetime

def main():
    
    results = requests.get('https://akaditi.com/')

    if results.status_code == 200:
        notification("Server is alive")
    else:
        notification("Server Down")
        logerror("Server went down at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    
    Timer(5,main).start()

def notification(args):
    data = {
        "text": args
    }

    webhook = os.environ.get("slack_webhook")
    requests.post(webhook, json.dumps(data))

def logerror(error):
    file=open("/var/log/nodemonitor.log", "a+")
    file.write(error)
    file.close()


if __name__ == '__main__':
    main()