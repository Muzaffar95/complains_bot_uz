# ComplaintBot Loyihasi

## 📦 Tavsif
Telegram orqali shikoyatlarni qabul qiluvchi bot va FastAPI asosidagi admin panel.  
Ma'lumotlar PostgreSQL bazasida saqlanadi, PDF fayl hosil qiladi, Excelga eksport qiladi.  
Docker Compose va nginx orqali SSL bilan joylashtiriladi.

---

## 🚀 Ishga tushurish

### 1. Klonlash yoki arxivni ochish

```bash
git clone https://github.com/your-org/complaint_bot_project.git
cd complaint_bot_project
```

### 2. .env faylini sozlash

`.env.example` asosida `.env` faylini yarating:

```bash
cp .env.example .env
nano .env
```

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
