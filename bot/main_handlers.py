from telegram import Update, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.ext import (
    CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
)
from bot.db import SessionLocal
from bot.models import Complaint
from bot.pdf_generator import generate_pdf
from bot.config import ADMINS, BOT_TOKEN, NOTIFY_CHAT_ID
from bot.handlers.admin_auth import auth_panel  # ← добавлено

FIO, TEL, COMMENT = range(3)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Xush kelibsiz! Shikoyat yuborish uchun /report buyrugʻini bering.")

# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Buyruqlar:\n/report - подать жалобу\n/FIO - F.I.SH.\n/tel - номер телефона\n/comment - комментарий\n/accept - подтвердить"
    )

# /report
async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("F.I.SH.ni kiriting:")
    return FIO

# F.I.SH.
async def fio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["fio"] = update.message.text
    await update.message.reply_text("Telefon raqamingizni kiriting:")
    return TEL

# Telefon
async def tel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["tel"] = update.message.text
    await update.message.reply_text("Shikoyat matnini kiriting:")
    return COMMENT

# Izoh
async def comment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["comment"] = update.message.text
    await update.message.reply_text("Shikoyatni yuborish uchun /accept buyrugʻini bering.")
    return ConversationHandler.END

# /accept
async def accept(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    fio = context.user_data.get("fio", "Не указано")
    tel = context.user_data.get("tel", "Не указано")
    comment = context.user_data.get("comment", "Не указано")

    session = SessionLocal()
    complaint = Complaint(
        user_id=user_id,
        full_name=fio,
        phone=tel,
        comment=comment
    )
    session.add(complaint)
    session.commit()
    session.close()

    # Генерация PDF
    #pdf_file = generate_pdf(fio, tel, comment)
    #pdf_url = f"https://mdmgasn.uz/{pdf_file}"
    
    # Уведомление в Telegram-группу
    #bot = Bot(BOT_TOKEN)
    #await bot.send_message(
    #    chat_id=NOTIFY_CHAT_ID,
    #    text=(
    #        f"<b>📬 Yangi shikoyat!</b>\n\n"
    #        f"<b>F.I.SH.:</b> {fio}\n"
    #        f"<b>Telefon:</b> {tel}\n"
    #        f"<b>Izoh:</b> {comment}\n"
    #        f"<a href='{pdf_url}'>📎 PDF-ni ochish</a>"
    #    ),
    #    parse_mode="HTML"
    #)
    # Генерация PDF
    pdf_file = generate_pdf(fio, tel, comment)

    # Очистим путь от "./"
    pdf_file = pdf_file.lstrip("./")

    # Сформируем абсолютную ссылку
    pdf_url = f"https://mdmgasn.uz/{pdf_file}"

    # Уведомление в Telegram-группу
    bot = Bot(BOT_TOKEN)
    await bot.send_message(
        chat_id=NOTIFY_CHAT_ID,
        text=(
            f"📬 *Yangi shikoyat!*\n\n"
            f"*F.I.SH.:* {fio}\n"
            f"*Telefon:* {tel}\n"
            f"*Izoh:* {comment}\n"
            f"[📎 PDF-ni ochish]({pdf_url})"
        ),
        parse_mode="Markdown"
)



    await update.message.reply_text(f"Shikoyatning PDF fayli saqlandi: {pdf_file}")
    await update.message.reply_text("Shikoyat qabul qilindi. Rahmat!")

# Отмена
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Shikoyat bekor qilindi.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

# Найти Telegram ID
async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🆔 Sizning Telegram ID raqamingiz: {update.effective_user.id}")

def setup_handlers(app):
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("report", report)],
        states={
            FIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, fio)],
            TEL: [MessageHandler(filters.TEXT & ~filters.COMMAND, tel)],
            COMMENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, comment)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("accept", accept))
    app.add_handler(CommandHandler("id", get_id))
    app.add_handler(CommandHandler("adminpanel", auth_panel))  # ← добавлено
    app.add_handler(conv_handler)

