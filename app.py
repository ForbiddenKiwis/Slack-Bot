from flask import Flask, request, make_response

import os
import json
import hmac
import hashlib
import time

from slack_sdk import WebClient
from dotenv import load_dotenv

load_dotenv()

SLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

print("[DEBUG] SLACK_BOT_TOKEN:", SLACK_TOKEN)
print("[DEBUG] SLACK_SIGNING_SECRET:", SLACK_SIGNING_SECRET)

app = Flask(__name__)
client = WebClient(token=SLACK_TOKEN)

def verify_slack_request(req):
    timestamp = req.headers.get('X-Slack-Request-Timestamp')
    if abs(time.time() - int(timestamp)) > 60 * 5:
        return False
    
    sig_basestring = f'v0:{timestamp}:{req.get_data(as_text=True)}'
    my_signature = 'v0=' + hmac.new(
        SLACK_SIGNING_SECRET.encode(),
        sig_basestring.encode(),
        hashlib.sha256
    ).hexdigest()
    slack_signature = req.headers.get('X-Slack-Signature')
    return hmac.compare_digest(my_signature,slack_signature)

@app.route("/slack/events", methods=["POST"])
def slack_events():
    if not verify_slack_request(request):
        return make_response("Invalid signature", 403)
    
    payload = request.get_json()

    if "challenge" in payload:
        return make_response(payload["challenge"], 200)
    
    event = payload.get("event", {})
    if event.get("type") == "app_mention":
        user = event.get("user")
        channel = event.get("channel")
        client.chat_postMessage(channel=channel, text=f"👋 Hi <@{user}>!")

        return make_response("", 200)
    
if __name__ == "__main__":
    from pyngrok import ngrok
    port = int(os.getenv("PORT", 3000))
    public_url = ngrok.connect(port)
    print(f"🌐 Public URL: {public_url}")
    app.run(port=port)
