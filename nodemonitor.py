from threading import Timer
import json,os,datetime,requests

def main():
    
    results = requests.get('<node address>')

    if results.status_code == 200:
        print("Server is alive")
    else:
        notification("Server Down")
        logerror("Server went down at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    
    Timer(5,main).start()

def notification(arg):
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