
import os
from slackclient import SlackClient

def sendPng(image):
    slack_token = os.environ["SLACK_API_TOKEN"]
    sc = SlackClient(slack_token)

    resp = sc.api_call(
        "files.upload",
        channels="#general",
        file=image,
        title="Test upload"
    )
    print (resp)
    