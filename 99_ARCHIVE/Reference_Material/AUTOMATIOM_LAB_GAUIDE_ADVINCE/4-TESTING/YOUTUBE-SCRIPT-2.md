# 🎬 YOUTUBE SCRIPT 2 - "Complete Setup Guide (15 minutes)"

## VIDEO SPECS
- Duration: 15 minutes (Step-by-step tutorial)
- Format: Screen recording + voiceover
- Title: "Telegram Affiliate Bot - Complete Setup (No Code)"
- Thumbnail: Screenshot of bot posting + "COMPLETE GUIDE"

## SCRIPT

### INTRO (0:00-0:30)

"Welcome! In this video, I'll walk you through the COMPLETE setup.

By the end, you'll have a bot posting deals automatically.

Let's go!"

---

### PART 1: CREATE TELEGRAM BOT (0:30-3:00)

[SCREEN: Telegram search]

"First, open Telegram and search for @BotFather

(I'll put a link in description)"

[SCREEN: BotFather chat]

"Send /newbot

He'll ask for a name. Type: 'My Affiliate Bot'

Then username. Something like: my_automation_bot_123

He'll give you a TOKEN. This is like a password. Copy it."

[HIGHLIGHT: Show the token clearly]

"Save this somewhere safe. You'll need it next."

---

### PART 2: CREATE TELEGRAM CHANNEL (3:00-5:00)

[SCREEN: Telegram home]

"Now create a channel for your deals.

Tap the pencil icon → New Channel

Name: 'Best Deals Daily' (or whatever)

Make it PUBLIC (important!)

Description: 'Daily deals and discounts'

Create it."

[SCREEN: Channel created]

"Now get your Channel ID.

Go to your channel → Click three dots → Edit

Copy the URL. The number after 'c/' is your Channel ID.

Save this too."

---

### PART 3: SET UP n8n (5:00-8:00)

[SCREEN: n8n dashboard]

"Go to n8n (localhost:5678 or your n8n URL)

Click + New → Import from file

Select the affiliate-bot-template.json file

(You downloaded this from Gumroad)"

[SCREEN: Workflow imported]

"Great! The workflow is now in n8n.

This is what will run automatically.

But we need to add your credentials first."

---

### PART 4: ADD CREDENTIALS (8:00-11:00)

[SCREEN: Click on Telegram node]

"Click on the 'Post to Telegram' node

In the URL field, find: {{ $env.TELEGRAM_BOT_TOKEN }}

Replace it with your actual token:

https://api.telegram.org/bot[YOUR_TOKEN_HERE]/sendMessage"

[SCREEN: Paste token]

"Now below that, find: {{ $env.TELEGRAM_CHANNEL_ID }}

Replace with your channel ID: @yourchannel or the numeric ID"

[SCREEN: Save]

"Click Save."

---

### PART 5: SETUP GOOGLE SHEETS (11:00-13:00)

[SCREEN: n8n log node]

"Now for tracking. Click on 'Google Sheets' node.

You need to authenticate with your Google account.

Click the lock icon → Select or connect new

Google will ask permission. Accept it.

Now select your spreadsheet:
- Create new or use existing
- This will log every deal posted"

[SCREEN: Sheet creation]

"Add columns:
A: deal_id
B: product_name
C: price
D: affiliate_link
E: posted_time
F: conversions"

---

### PART 6: SET SCHEDULE (13:00-14:00)

[SCREEN: Trigger node]

"Now when should it run?

Click the Cron trigger (the clock icon)

Set timing:
- Every 2 hours (12 posts/day)
- Or daily at 9 AM

Your choice. I recommend every 2 hours for more posts."

[SCREEN: Set cron]

"Good. Now we're ready to test!"

---

### PART 7: TEST (14:00-14:45)

[SCREEN: Execute button]

"Click the Execute button (play icon)

If it works, you should see green checkmarks.

Go to your Telegram channel.

You should see a post! 

Check your Google Sheet.

You should see a log entry!

SUCCESS!"

---

### OUTRO (14:45-15:00)

"That's it! Your bot is now running.

It'll post automatically on the schedule you set.

Watch your Google Sheet for earnings.

Questions? Comment below.

Subscribe for more automation guides!"

---

## SCREEN RECORDING CHECKLIST

✅ Telegram search for @BotFather
✅ BotFather conversation  
✅ Token creation
✅ Channel creation
✅ n8n dashboard
✅ Import workflow
✅ Add credentials
✅ Google Sheets setup
✅ Schedule settings
✅ Execute test
✅ Successful result in Telegram
✅ Google Sheet log

## AUDIO NOTES

- Speak slowly and clearly
- Pause between steps (let people catch up)
- Highlight important steps
- Repeat key information

## YOUTUBE DESCRIPTION

```
Complete step-by-step setup for Telegram affiliate bot.

⏰ TIMESTAMPS:
0:00 Intro
0:30 Create Telegram Bot
3:00 Create Channel
5:00 Setup n8n
8:00 Add Credentials
11:00 Google Sheets
13:00 Set Schedule
14:00 Test it

🔗 DOWNLOADS:
Template: [gumroad link]
Bot Father: @BotFather on Telegram

💡 WHAT YOU'LL NEED:
- n8n running (free)
- Telegram account
- Google account
- 15 minutes

🎯 RESULT:
After this video, you'll have:
- Automatic deal posting
- Earnings tracking
- Daily reports

Start earning while you sleep!

#n8n #automation #affiliatemarketing #telegram
```

