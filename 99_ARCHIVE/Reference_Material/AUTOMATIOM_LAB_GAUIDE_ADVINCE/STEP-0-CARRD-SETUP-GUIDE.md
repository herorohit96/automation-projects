# 🚀 STEP 0: CARRD LINKTREE SETUP (Copy-Paste)

## Ab start karte hain. Ye exactly follow karna.

---

## 📋 PART 1: CARRD ACCOUNT BANAO (5 min)

1. Go to: **https://carrd.co**
2. Top-right pe click karo: **"Sign Up"**
3. Email + Password daal kar account banao
4. **Confirm email** (check inbox)

---

## 🎨 PART 2: CARRD SITE CREATE KARO (3 min)

1. Carrd dashboard mein ho to: **"New Site"** button click karo
2. Site name: `automation-hub` ya `automation-business` (jo bhi pasand)
3. Choose template: **"Blank"** (empty se shuru karenge)
4. Click **"Create"**

Now tu Carrd editor mein hoga.

---

## 📝 PART 3: HTML PASTE KARO (5 min)

#### Step 3.1: Add Element
1. Left side mein **"+"** button dekho
2. Scroll down → **"Custom Code"** option click karo
3. Box add hoga

#### Step 3.2: Paste HTML
Copy-paste ye **POORA HTML** neeche diya gaya box mein:

```html
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Automation Business Solutions</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 500px;
            padding: 40px;
            text-align: center;
            animation: slideUp 0.6s ease-out;
        }
        
        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .header {
            margin-bottom: 30px;
        }
        
        .avatar {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0 auto 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 60px;
        }
        
        h1 {
            color: #333;
            font-size: 28px;
            margin-bottom: 10px;
        }
        
        .subtitle {
            color: #666;
            font-size: 14px;
            margin-bottom: 10px;
        }
        
        .tagline {
            color: #888;
            font-size: 13px;
            margin-bottom: 30px;
            font-style: italic;
        }
        
        .links-section {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 30px;
        }
        
        .link-btn {
            display: block;
            padding: 14px 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            font-size: 15px;
            transition: all 0.3s ease;
            border: 2px solid transparent;
        }
        
        .link-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }
        
        .link-btn.secondary {
            background: white;
            color: #667eea;
            border: 2px solid #667eea;
        }
        
        .link-btn.secondary:hover {
            background: #f8f9ff;
        }
        
        .stats {
            background: #f8f9ff;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 10px;
        }
        
        .stat-item {
            font-size: 12px;
        }
        
        .stat-number {
            font-size: 20px;
            font-weight: bold;
            color: #667eea;
        }
        
        .stat-label {
            color: #888;
            margin-top: 5px;
        }
        
        .social {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
        }
        
        .social a {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #f0f0f0;
            color: #667eea;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .social a:hover {
            background: #667eea;
            color: white;
            transform: scale(1.1);
        }
        
        .footer {
            font-size: 12px;
            color: #999;
            margin-top: 20px;
            border-top: 1px solid #eee;
            padding-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="avatar">🚀</div>
            <h1>Automation Business</h1>
            <div class="subtitle">Ready-to-Use n8n Workflows & Setup Services</div>
            <div class="tagline">15+ Professional Workflows • Email Automation • Telegram Bots • Setup Support</div>
        </div>
        
        <div class="stats">
            <div class="stat-item">
                <div class="stat-number">18+</div>
                <div class="stat-label">Workflows</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">500+</div>
                <div class="stat-label">Users</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">4.9⭐</div>
                <div class="stat-label">Rating</div>
            </div>
        </div>
        
        <div class="links-section">
            <a href="https://gumroad.com/yourname" class="link-btn" target="_blank">
                💰 Buy Templates (₹7,999)
            </a>
            <a href="https://fiverr.com/yourname" class="link-btn" target="_blank">
                🛠️ Hire for Setup Service
            </a>
            <a href="https://t.me/yourgroup" class="link-btn secondary" target="_blank">
                💬 Join Telegram Community
            </a>
            <a href="https://mailchimp.com/yourform" class="link-btn secondary" target="_blank">
                📧 Join Email List (Free Training)
            </a>
        </div>
        
        <div class="social">
            <a href="https://twitter.com/yourname" target="_blank">𝕏</a>
            <a href="https://linkedin.com/in/yourname" target="_blank">in</a>
            <a href="https://instagram.com/yourname" target="_blank">📷</a>
        </div>
        
        <div class="footer">
            Made with 🖤 | Privacy Policy
        </div>
    </div>
</body>
</html>
```

---

## ⚙️ PART 4: LINKS CUSTOMIZE KARO

Ab HTML mein ye URLs change karo:

| Replace | With |
|---------|------|
| `https://gumroad.com/yourname` | Tera actual Gumroad link (baad mein) |
| `https://fiverr.com/yourname` | Tera actual Fiverr profile URL |
| `https://t.me/yourgroup` | Tera Telegram group/channel link |
| `https://mailchimp.com/yourform` | Tera email signup form |
| `https://twitter.com/yourname` | Tera Twitter profile |
| `https://linkedin.com/in/yourname` | Tera LinkedIn profile |
| `https://instagram.com/yourname` | Tera Instagram handle |

**For Now:** Bas `#` daal de placeholder mein, baad mein update karega.

Example: `<a href="#" class="link-btn">`

---

## 🎯 PART 5: CARRD PUBLISH KARO (1 min)

1. Top-right mein **"Publish"** button dekho
2. Click karo
3. Carrd apko free domain dega: `yourname.carrd.co`

**DONE!** Tu live ho gaya! 🎉

---

## 📊 STATS UPDATE

Stats mein ye change kar:
- `18+` → actual number of workflows
- `500+` → actual customers (start with 0, later update)
- `4.9⭐` → actual rating (start with 5.0)

Ye automatically update hona chahiye tera growth ke sath.

---

## ✅ NEXT (Fiverr Step)

Jab ye publish ho jaye, reply: **"CARRD DONE"**

Main then FIVERR setup guide dunga. 🚀
