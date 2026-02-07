# 📖 SETUP GUIDE - Service 2: Telegram Post + Logging

## What You'll Get
Auto-posts content to your Telegram channel on a schedule and tracks everything.

## Prerequisites
- n8n running
- Telegram bot token
- Telegram channel (or group)
- Google Sheets (for logging)

## Step-by-Step Setup

### STEP 1: Create Bot & Get Channel ID
1. Create bot with @BotFather (same as Service 1)
2. Copy your channel ID:
   - Make your channel public
   - Go to: `t.me/yourchannel`
   - Channel ID = the number after `c/`

### STEP 2: Import Workflow
1. n8n → **+ New** → **Import from file**
2. Select `template-2-telegram-post-logging.json`

### STEP 3: Setup Google Sheets Integration
1. Click on "Log Post" node
2. Connect your Google account
3. Create new spreadsheet
4. Add columns: `post_id`, `content`, `posted_at`, `status`

### STEP 4: Configure Schedule
1. Click "Schedule Trigger" node
2. Set timing:
   - **Time:** 9:00 AM (adjust as needed)
   - **Frequency:** Daily/Weekly/Custom

### STEP 5: Add Your Content
1. Click "Get Post Data" node
2. Modify content to post:
   ```
   "content": "Your post text here #automation #n8n"
   ```

### STEP 6: Add Credentials
1. Replace `{{ $env.TELEGRAM_BOT_TOKEN }}` with your token
2. Replace `{{ $env.TELEGRAM_CHANNEL_ID }}` with your channel ID

### STEP 7: Test
1. Click **Execute workflow**
2. Should post to your channel instantly!
3. Check Google Sheets for log entry

## Advanced: Connect to Content Source

### Option A: Google Sheets (Recommended)
```
Schedule → Read from Google Sheets → Post → Log
```

### Option B: RSS Feed
```
RSS Trigger → Format → Post → Log
```

### Option C: API/Webhook
```
Webhook → Format → Post → Log
```

## What You Can Track
- ✅ Post ID
- ✅ Posted time
- ✅ View count (if using analytics)
- ✅ Click-through rate
- ✅ Engagement

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Posts aren't showing | Channel ID is wrong |
| Google Sheets error | Re-authenticate account |
| Schedule not running | n8n executions are off |

## Upsells
- Add: **View tracking** (Google Analytics link)
- Add: **A/B testing** (two versions, compare)
- Add: **AI generation** (content created automatically)

---

**Setup time: 20-30 minutes**
**Difficulty: Intermediate**
**Value created: ₹5,999+**
