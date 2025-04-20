---

## 🧪 PyCharm orqali lokal test

1. Loyihani GitHubdan yuklab oling va qulay papkaga joylashtiring.
2. PyCharm dasturida loyihani oching.
3. Terminalda quyidagi buyruq bilan kerakli kutubxonalarni o‘rnating:

```bash
pip install -r complaint_bot_project/requirements.txt
```

4. `.env` faylini yarating(agar mavjud bo'lmasa) va quyidagilarni belgilang:

```env
TELEGRAM_BOT_TOKEN=telegram_token
```

5. Quyidagi faylni ishga tushiring:

```bash
python complaint_bot_project/main_polling.py
```

🔄 Bot `polling` rejimida ishga tushadi va webhook talab qilinmaydi.