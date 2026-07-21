from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from database import connect
from config import BOT_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    db = connect()
    cursor = db.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id BIGINT PRIMARY KEY, username VARCHAR(100))"
    )

    cursor.execute(
        "INSERT IGNORE INTO users VALUES(%s,%s)",
        (user.id, user.username)
    )

    db.commit()

    await update.message.reply_text(
        "🔥 Welcome to PANNEL SHOP\n\nUse /status"
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "✅ Your account is active"
    )


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("status", status))

print("Bot Running...")

app.run_polling()
