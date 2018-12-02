
import os
from slackclient import SlackClient

def simple_send_png(image, title):
    slack_token = os.environ["SLACK_API_TOKEN"]
    sc = SlackClient(slack_token)

    resp = sc.api_call(
        "files.upload",
        channels="#general",
        file=image,
        title=title
    )
    return resp

def retrying_send_png(image, title):
    resp = simple_send_png(image, title)
    if resp["ok"]:
        print("Image posted successfully")
    # If the message failed, check for rate limit headers in the response
    elif resp["ok"] is False and resp["headers"]["Retry-After"]:
        # The `Retry-After` header will tell you how long to wait before retrying
        delay = int(resp["headers"]["Retry-After"])
        print("Rate limited. Retrying in " + str(delay) + " seconds")
        time.sleep(delay)
        simple_send_png(image, "#general")

    