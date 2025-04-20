from telegram.ext import ApplicationBuilder
from bot.config import BOT_TOKEN
from bot.main_handlers import setup_handlers

async def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    setup_handlers(application)
    print("✅ Бот запущен в режиме polling")
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())