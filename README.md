<<<<<<< HEAD
---

## 🧪 PyCharm orqali lokal test

1. Loyihani GitHubdan yuklab oling va qulay papkaga joylashtiring.
2. PyCharm dasturida loyihani oching.
3. Terminalda quyidagi buyruq bilan kerakli kutubxonalarni o‘rnating:
=======
# ComplaintBot Loyihasi

## 📦 Tavsif
Telegram orqali shikoyatlarni qabul qiluvchi bot va FastAPI asosidagi admin panel.  
Ma'lumotlar PostgreSQL bazasida saqlanadi, PDF fayl hosil qiladi, Excelga eksport qiladi.  
Docker Compose va nginx orqali SSL bilan joylashtiriladi.

---

## 🚀 Ishga tushurish

### 1. Klonlash yoki arxivni ochish
>>>>>>> 58f2bd1d32367b36e6700cd99b9bf5e84899d5bf

```bash
pip install -r complaint_bot_project/requirements.txt
```

<<<<<<< HEAD
4. `.env` faylini yarating(agar mavjud bo'lmasa) va quyidagilarni belgilang:

```env
TELEGRAM_BOT_TOKEN=telegram_token
```

5. Quyidagi faylni ishga tushiring:
=======
### 2. .env faylini sozlash

`.env.example` asosida `.env` faylini yarating:
>>>>>>> 58f2bd1d32367b36e6700cd99b9bf5e84899d5bf

```bash
python complaint_bot_project/main_polling.py
```

<<<<<<< HEAD
🔄 Bot `polling` rejimida ishga tushadi va webhook talab qilinmaydi.
=======
Quyidagilarni kiriting:

- `TELEGRAM_BOT_TOKEN=telegram_bot_tokeningiz`
- `WEBHOOK_URL=https://saytingiz.com/webhook`
- `POSTGRES_*` — ma'lumotlar bazasiga ulanish

### 3. Docker Compose orqali ishga tushirish

```bash
docker-compose up --build -d
```

---

## 🌐 Kirish

- Bot: `@your_bot` → /start
- Admin panel: `https://saytingiz.com/html?token=...`
- Token olish:

```bash
curl -X POST https://saytingiz.com/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin"
```

---

## 🛠 Nginx + SSL

`/etc/nginx/sites-available/` katalogida kerakli sozlamalarni belgilang, certbot orqali SSL sertifikat oling.

---

## 📂 Tuzilishi

- `bot/` — Telegram bot kodi
- `web_panel/` — FastAPI asosidagi admin panel
- `pdfs/` — yaratilgan PDF shikoyatlar
- `database/` — SQL yaratish fayllari
- `docker-compose.yml` — ishga tushirish uchun konfiguratsiya

---

## 📞 Aloqa
Muallif: 🧑‍💻 Muzaffar Abdulxamitov
>>>>>>> 58f2bd1d32367b36e6700cd99b9bf5e84899d5bf
