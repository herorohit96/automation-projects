# 📖 SETUP GUIDE - Service 1: Telegram Command Bot

## What You'll Get
A bot that automatically responds to commands in Telegram.

## Prerequisites
- n8n running (http://localhost:5678)
- Telegram bot token (from @BotFather)
- Basic understanding of n8n

## Step-by-Step Setup

### STEP 1: Create Your Telegram Bot
1. Open Telegram
2. Search for **@BotFather**
3. Send `/newbot`
4. Follow instructions:
   - Bot name: `My Automation Bot`
   - Username: `my_automation_bot_[random]`
5. **Copy the TOKEN** (you'll need it)

### STEP 2: Import Workflow in n8n
1. Go to n8n (http://localhost:5678)
2. Click **+ New** → **Import from file**
3. Select `template-1-telegram-command-bot.json`
4. Click **Import**

### STEP 3: Add Your Bot Token
1. Click on "Send Telegram Reply" node
2. In the URL field, find: `{{ $env.TELEGRAM_BOT_TOKEN }}`
3. Replace with your actual token:
   ```
   https://api.telegram.org/bot123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef/sendMessage
   ```

### STEP 4: Set Webhook URL
1. Find the **Webhook** node
2. Copy the webhook URL shown
3. Open this in browser (replace BOT_TOKEN):
   ```
   https://api.telegram.org/botBOT_TOKEN/setWebhook?url=YOUR_WEBHOOK_URL
   ```
4. You should see: `{"ok":true}`

### STEP 5: Add Commands
Edit the "Command Handler" function to add more commands:

```javascript
if (text === '/status') {
  return [{json: {reply: 'All systems go!'}}];
}
else if (text === '/help') {
  return [{json: {reply: 'Available: /start, /help, /status'}}];
}
```

### STEP 6: Test
1. Go to Telegram
2. Find your bot by username
3. Send `/start`
4. Bot should reply automatically!

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Bot doesn't respond | Check token is correct |
| Error 400 | Webhook URL is wrong |
| Timeout | n8n might be down, restart |

## What's Next?
- Add more commands
- Connect to databases
- Build complex workflows

## Support
Having issues? DM @YourSupport on Telegram

---

## FILES INCLUDED
- `template-1-telegram-command-bot.json` (workflow)
- `setup-guide.md` (this file)
- `FAQ.md` (answers to common questions)

---

**Setup time: 10-15 minutes**
**Difficulty: Beginner**
**Value created: ₹2,999+**
