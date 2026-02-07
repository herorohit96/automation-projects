# 🤖 STEP 2.0: CUSTOMER AUTOMATION (Email + Telegram Triggers)

## Context
Teri funnel ban gayi:
- Lead magnet landing page ✅
- 7-email sequence ✅
- Social media posts ✅

Ab automation setup karna.

Email trigger automatically bhej dena.
Telegram bot automatically welcome message send karna.
Everything hands-off.

---

## PART 1: EMAIL AUTOMATION TRIGGERS

### What is Email Automation?

Instead of manually sending 7 emails...
Automation sends them automatically based on triggers.

```
Customer signs up
    ↓
Trigger 1: Email 1 (Welcome)
    ↓ (next day)
Trigger 2: Email 2 (Social proof)
    ↓ (next day)
Trigger 3: Email 3 (Premium offer)
    ↓ (next day)
Trigger 4: Email 4 (Objections)
...and so on
```

Result: 0 manual work. Runs forever.

---

## PART 2: EMAIL SERVICE PROVIDER SETUP

### Using MailerLite (Recommended)

#### Step 1: Create Account
```
1. Go to www.mailerlite.com
2. Sign up (free account)
3. Confirm email
4. You're in!
```

#### Step 2: Create Automation Sequence
```
In MailerLite:

1. Click "Automations" (left menu)
2. Click "New Automation"
3. Choose trigger: "Subscriber added to group"
4. Select group: "Free Template Subscribers"
5. Click "Continue"
```

#### Step 3: Add Email Steps
```
Step 1: Add action → Send email
  Select: Email 1 (Welcome)
  Delay: 0 minutes (send immediately)
  
Step 2: Add action → Send email
  Select: Email 2 (Social proof)
  Delay: 24 hours
  
Step 3: Add action → Send email
  Select: Email 3 (Premium offer)
  Delay: 48 hours
  
Step 4: Add action → Send email
  Select: Email 4 (Objections)
  Delay: 72 hours

...continue for all 7 emails
```

#### Step 4: Save & Activate
```
Click "Activate" button
Done! Automation runs forever.
```

---

## PART 3: LANDING PAGE TO EMAIL SETUP

### Connect Form to Email List

#### In MailerLite:

```
1. Go to "Forms" (left menu)
2. Create new form
3. Name: "Free Template Signup"
4. Type: Embedded (for Carrd)
5. Add field: Email (required)
6. Add field: First Name (optional)
7. Add field: Telegram ID (optional)
8. Click "Save form"
```

#### Get Form Code:

```
Form created.
Now copy the embed code.

1. In form, click "Embed"
2. Choose "Popup" or "Embedded"
3. Copy the code
4. Paste into Carrd
```

#### In Carrd (Your Landing Page):

```
1. Edit landing page
2. Click "Add element"
3. Choose "Embed"
4. Paste MailerLite form code
5. Save
6. Test by entering email
```

#### Test the Flow:

```
1. Go to your landing page
2. Enter email (test@example.com)
3. Submit
4. Check MailerLite: Subscriber should appear in list
5. Check email: Should receive Email 1 immediately
6. Wait 24 hours: Email 2 should arrive
```

---

## PART 4: TELEGRAM BOT AUTOMATION

### What is Telegram Bot Automation?

Your customer signs up with email.
Telegram bot automatically sends them:
- Welcome message
- Setup guide
- Support info

```
Customer supplies Telegram ID
    ↓
Telegram Bot triggers welcome sequence
    ↓
Bot sends setup guide
    ↓
Bot offers support
```

---

### How to Set Up Telegram Bot Automation

#### Step 1: Create Telegram Bot

```
1. Open Telegram
2. Search for "@BotFather"
3. Click Start
4. Type: /newbot
5. Name your bot: "Rohan's Affiliate Bot" (your name)
6. Choose username: "rohan_affiliate_bot" (must be unique)
7. Copy the TOKEN (you'll use this)

Example token: 123456789:ABCDEFGHIJKLMNOPQRSTuvwxyz

Keep this secret!
```

#### Step 2: Connect to n8n (Your Automation Platform)

Since you already have n8n running:

```
1. Log into your n8n (localhost:5678)
2. Create new workflow
3. Name: "Telegram Customer Welcome Bot"
4. Add trigger: "Webhook" 
5. Method: POST
6. Copy webhook URL (you'll use this)
```

#### Step 3: Create Email Trigger to Telegram

In MailerLite + n8n integration:

```
When customer signs up:
1. MailerLite sends webhook to n8n
2. n8n receives email + Telegram ID
3. n8n sends Telegram message
4. Bot sends welcome sequence

Set it up:
1. In MailerLite automation
2. Add action: "Webhook"
3. Enter n8n webhook URL
4. Map fields: Email, Name, Telegram ID
5. Save
```

---

## PART 5: TELEGRAM BOT WELCOME SEQUENCE

### What the Bot Will Send

#### Message 1 (Immediately on signup)
```
Hi Rohan! 👋

Welcome to the community!

Your free template is on the way via email.

Check your inbox (including spam folder).

Questions? I'm here 24/7.

Just type your question here.
```

#### Message 2 (After 2 hours)
```
Quick question: Have you started setup?

If yes → Tell me! I'm proud.

If no → What's stopping you? I can help.

Setup takes only 15 minutes.
```

#### Message 3 (After 6 hours)
```
Your setup guide is attached.

Follow these steps:
1. Login to n8n
2. Copy the workflow
3. Paste it
4. Connect Telegram
5. Done!

Need help? Type /help
```

#### Message 4 (After 12 hours)
```
Pro tip: Most people who setup in first 24 hours make ₹1K by day 5.

Those who wait? Takes longer.

Time to setup? Now 🚀

Questions? Type /support
```

#### Message 5 (After 24 hours)
```
It's been a day.

Have you made your first ₹100 yet? 

If yes → Tell me! Screenshot?

If no → Let's troubleshoot.

What's the issue?
```

---

## PART 6: BUILD THE TELEGRAM BOT IN N8N

### Full Workflow Code

```json
{
  "name": "Telegram Customer Welcome Bot",
  "nodes": [
    {
      "parameters": {
        "path": "telegram-webhook",
        "method": "POST"
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "javaScriptCode": "// Parse incoming data from MailerLite\nconst data = $input.first().json;\n\nreturn {\n  email: data.email,\n  name: data.first_name || 'Friend',\n  telegram_id: data.custom_fields?.telegram_id,\n  signup_time: new Date().toISOString()\n};"
      },
      "name": "Parse Signup Data",
      "type": "n8n-nodes-base.code",
      "typeVersion": 1,
      "position": [450, 300]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.telegram.org/bot{{ $vars.TELEGRAM_BOT_TOKEN }}/sendMessage",
        "bodyParameters": [
          {
            "name": "chat_id",
            "value": "={{ $input.first().json.telegram_id }}"
          },
          {
            "name": "text",
            "value": "Hi {{ $input.first().json.name }}! 👋\n\nWelcome to the community!\n\nYour free template is on the way via email.\n\nCheck your inbox (including spam folder).\n\nQuestions? I'm here 24/7.\n\nJust type your question here."
          }
        ]
      },
      "name": "Send Welcome Message",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 2,
      "position": [650, 300]
    },
    {
      "parameters": {
        "triggerTimes": [
          {
            "mode": "hours",
            "value": 2
          }
        ]
      },
      "name": "Wait 2 Hours",
      "type": "n8n-nodes-base.wait",
      "typeVersion": 1,
      "position": [850, 300]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.telegram.org/bot{{ $vars.TELEGRAM_BOT_TOKEN }}/sendMessage",
        "bodyParameters": [
          {
            "name": "chat_id",
            "value": "={{ $input.first().json.telegram_id }}"
          },
          {
            "name": "text",
            "value": "Quick question: Have you started setup?\n\nIf yes → Tell me! I'm proud.\n\nIf no → What's stopping you? I can help.\n\nSetup takes only 15 minutes."
          }
        ]
      },
      "name": "Send Follow-up Message",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 2,
      "position": [1050, 300]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Parse Signup Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parse Signup Data": {
      "main": [
        [
          {
            "node": "Send Welcome Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send Welcome Message": {
      "main": [
        [
          {
            "node": "Wait 2 Hours",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wait 2 Hours": {
      "main": [
        [
          {
            "node": "Send Follow-up Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

### How to Use This Code

```
1. In n8n, click "New"
2. Click "Import from URL" or "Import from clipboard"
3. Paste the JSON code above
4. Click Import
5. You now have the workflow!
6. Click "Edit" on telegram-webhook node
7. Copy your webhook URL
8. Add it to MailerLite (see Part 4)
9. Activate workflow (click play button)
```

---

## PART 7: SETUP CHECKLIST

### Week 1: Email Automation

- [ ] Create MailerLite account
- [ ] Paste 7 emails into MailerLite
- [ ] Create form in MailerLite
- [ ] Get form embed code
- [ ] Paste form code into Carrd
- [ ] Test: Submit form → Emails arrive
- [ ] Activate automation sequence

### Week 2: Telegram Bot

- [ ] Create Telegram bot (@BotFather)
- [ ] Get bot token
- [ ] Create n8n workflow (import JSON)
- [ ] Test bot sends messages
- [ ] Connect MailerLite → n8n webhook
- [ ] Test: Signup → Telegram message arrives

### Week 3: Testing & Optimization

- [ ] Send test email (yourself)
- [ ] Send test Telegram message
- [ ] Check email opens, clicks
- [ ] Optimize based on data
- [ ] Monitor conversion rates
- [ ] Track which email converts best

---

## PART 8: TROUBLESHOOTING

### Problem: Emails not arriving

**Solution:**
1. Check MailerLite list count (did subscriber add?)
2. Check automation is "Active"
3. Check email content (typos, formatting)
4. Check spam folder
5. Try sending test email manually

### Problem: Telegram bot not sending messages

**Solution:**
1. Check bot token is correct
2. Check Telegram ID is valid
3. Check n8n workflow is "Active"
4. Check webhook URL is correct
5. Test bot manually: /start command

### Problem: Form not submitting

**Solution:**
1. Check form code is pasted correctly
2. Clear browser cache
3. Test on different browser
4. Test on mobile
5. Check MailerLite API key (if custom integration)

---

## PART 9: EXPECTED RESULTS

**If everything works:**

```
Day 1:
- 10 signups
- 10 welcome emails sent
- 10 Telegram messages sent
- 7 opens

Day 7:
- 70 signups
- 70 welcome sequences started
- ~10 conversions to premium
- ₹79,990 revenue

Day 30:
- 300 signups
- 300 sequences active
- ~30 conversions
- ₹239,970 revenue
```

---

## 🚀 QUICK ACTION

1. **Setup MailerLite** (free account)
2. **Create automation** (7 emails)
3. **Create form** (get embed code)
4. **Paste form into Carrd** (landing page)
5. **Create Telegram bot** (@BotFather)
6. **Import n8n workflow** (JSON code)
7. **Test everything** (submit form → check emails + Telegram)
8. **Activate** (go live!)

---

**STEP 2.0 COMPLETE.**

**NEXT: STEP 2.1 (Customer support automation - FAQ bot + email responder)**

Chalo continue! 🚀
