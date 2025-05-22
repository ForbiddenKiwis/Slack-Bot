# Slack Bot

A simple Slack bot built with Flask that listens for Slack events and responds to app mentions. The bot verifies Slack request signatures for security and uses `ngrok` to expose the local server to the internet during development.

---

## Features

- Verifies Slack request signature using your Slack Signing Secret
- Responds to `app_mention` events with a friendly greeting
- Handles Slack URL verification challenge automatically
- Uses `ngrok` for exposing the local Flask server with a public URL

---

## Prerequisites

- Python 3.7 or higher
- Slack App with:
  - Bot Token (`SLACK_BOT_TOKEN`)
  - Signing Secret (`SLACK_SIGNING_SECRET`)
- `ngrok` installed or use the Python package `pyngrok`
- `pip` package manager

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/slack-bot.git
cd slack-bot
```

### 2. Create and activate a virtual environment (recommended)
```bash
python -m venv venv
```
#### On macOS/Linux:
```
source venv/bin/activate
```
#### On Windows:
```
venv\Scripts\activate
```

### 3. Install dependencies
#### Dependencies
- Flask
- python-dotenv
- slack-sdk
- pyngrok

You can use this command to download the dependencies in the terminal of you IDE.
```
pip install Flask python-dotenv slack-sdk pyngrok
```
  

### 4. Create .env file
Create a .env file in the project root with the following variables:
```
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_SIGNING_SECRET=your-signing-secret
PORT=3000
```
Replace the values with your actual Slack app credentials.

## Running the Bot
Start the Flask app:
```
python app.py
```
The script will automatically create a public URL using ngrok and print it in the console, for example:
```
🌐 Public URL: http://abcd1234.ngrok.io
```
Use this URL in your Slack app's Event Subscriptions as the Request URL with the suffix /slack/events, e.g.,
```
http://abcd1234.ngrok.io/slack/events
```

### Slack App Configuration
1. Go to your Slack app's Event Subscriptions page.
2. Enable Event Subscriptions.
3. Set the Request URL to the ngrok URL followed by /slack/events.
4. Subscribe to bot events:
5. app_mention
6. Install or reinstall the app to your workspace.

### Security
This app verifies requests from Slack using the signing secret to ensure security. The signature verification helps prevent unauthorized requests.

### Troubleshooting
- If your push to GitHub is blocked due to secret scanning, make sure .env is removed from Git history.
- If ngrok URL changes, update your Slack app Event Subscription URL.
- Ensure your Slack app has the correct OAuth scopes (chat:write, app_mentions:read).

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Author
ForbiddenKiwis 
