from dotenv import load_dotenv
import os
import requests
from langchain.agents import Tool

load_dotenv(override=True)

pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_user = os.getenv("PUSHOVER_USER")
pushover_url = "https://api.pushover.net/1/messages.json"


def _push(text: str):
    """Send a push notification to the user"""
    requests.post(
        pushover_url,
        data={"token": pushover_token, "user": pushover_user, "message": text},
    )
    return "success"


class PushProvider:
    def get_tools(self):
        return [
            Tool(
                name="send_push_notification",
                func=_push,
                description="Use this tool when you want to send a push notification",
            )
        ]