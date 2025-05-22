# Slack Bot with Flask

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
