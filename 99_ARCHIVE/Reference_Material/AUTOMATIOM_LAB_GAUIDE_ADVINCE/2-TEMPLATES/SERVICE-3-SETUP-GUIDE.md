# 📖 SETUP GUIDE - Service 3: Affiliate Telegram Bot (MOST PROFITABLE)

## What You'll Get
Automatic affiliate deal posting + tracking + earning reports.

## Prerequisites
- n8n running
- Telegram bot + channel
- Google Sheets (for tracking earnings)
- Affiliate accounts (Amazon, Flipkart, etc)
- RSS feeds or API access to deals

## PART 1: Setup Basic Bot

### STEP 1: Create Bot
1. @BotFather → `/newbot`
2. Save your **TOKEN**
3. Create public channel for deals
4. Save your **CHANNEL_ID**

### STEP 2: Import Workflow
1. n8n → **+ New** → **Import**
2. Select `template-3-affiliate-telegram-bot.json`

### STEP 3: Add Credentials
Replace these in the workflow:
- `{{ $env.TELEGRAM_BOT_TOKEN }}` → Your token
- `{{ $env.TELEGRAM_CHANNEL_ID }}` → Your channel
- `{{ $env.GOOGLE_SHEETS_ID }}` → Your sheet ID

### STEP 4: Configure Schedule
- Every 2 hours (deals posted 12x daily)
- Or custom timing

---

## PART 2: Connect Affiliate Sources

### Option A: Amazon Affiliate (EASIEST)
1. Sign up: amazon-adsystem.com
2. Get **Associates ID**
3. Install browser extension: **Amazon Assistant**
4. Get affiliate links automatically

**Add to workflow:**
```
RSS Feed: amazon.com/deal-rss
Parse deals → Add your associate ID → Post
```

### Option B: Flipkart Affiliate
1. Sign up: flipkart-ads.com
2. Get partner ID
3. Create API integration
4. Use our RSS feed

### Option C: Multiple Sources
1. Amazon RSS
2. Flipkart API
3. Custom deals API
4. Combine all → Post best deals

---

## PART 3: Setup Earnings Tracking

### Create Google Sheet:
Columns:
- `A: Deal ID`
- `B: Product Name`
- `C: Affiliate Link`
- `D: Posted Time`
- `E: Clicks` (track manually or via link shortener)
- `F: Conversions`
- `G: Commission (₹)`

### Link Shortener Setup (To Track Clicks)
1. Use: **Bitly** (free) or **Short.io**
2. Every affiliate link → short link
3. Get click data automatically
4. Calculate commission

### Example Earnings:
- 100 posts/day
- 1% conversion rate = 1 sale
- Average commission ₹200
- **₹200/day = ₹6,000/month (PASSIVE)**

---

## PART 4: Optimize for Earnings

### Best Practices
1. **Post at peak hours** (2 PM, 5 PM, 8 PM)
2. **Post high-margin deals** (electronics, fashion)
3. **Track what converts** (Sheets with notes)
4. **Test descriptions** (A/B test 2 versions)
5. **Build audience** (quality over quantity)

### Content Formula That Works
```
🔥 [PRODUCT NAME]

Price: ₹[Price]
Discount: [%] OFF! 

Link: [Shortened link]

⏰ Limited time! Check now
```

---

## PART 5: Scale to Multiple Channels

Once one channel works:
1. Create 2nd channel (same bot, different audience)
2. Create 3rd channel (different niche)
3. Multiply earnings by 3x

**Example:**
- 1 channel: ₹6,000/month
- 5 channels: ₹30,000/month
- 20 channels: ₹1,20,000/month

---

## Advanced Features (Add Later)

### Feature 1: Daily Earnings Report
```
Send automatic summary:
"Today's earnings: ₹450 (12 clicks, 3 sales)"
```

### Feature 2: Price Drop Alert
```
Monitor prices → Alert when drops > 20%
```

### Feature 3: Seasonal Deals
```
Fetch deals based on festival/season
Diwali special deals, New Year sales, etc.
```

### Feature 4: Customer Referral
```
"Share this bot, earn ₹100 per person"
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No deals showing | API/RSS feed is down |
| Wrong commission | Check affiliate % in settings |
| Bot blocked | Too many posts too fast, slow down |
| Low conversions | Improve product selection or descriptions |

---

## Revenue Streams from This Service

1. **Sell template:** ₹7,999 × 50 customers = ₹4,00,000
2. **Sell setup service:** ₹5,000 × 100 customers = ₹5,00,000
3. **Sell custom integration:** ₹10,000 × 50 = ₹5,00,000
4. **Monthly monitoring:** ₹2,000 × 30 customers = ₹6,00,000/month

**Year 1 potential: ₹20+ Lakhs** 🔥

---

**Setup time: 1-2 hours**
**Difficulty: Intermediate to Advanced**
**Value created: ₹7,999+ (one-time) to ₹6,000+/month (recurring)**
