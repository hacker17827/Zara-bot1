
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.constants import ParseMode
import json
import os

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace this later
USER_DB = "users.json"

app = Flask(__name__)

CHANNELS_BY_LANG = {
    "en": {
        "welcome": (
            "👋 Hi {name}!

"
            "50$ TO 5,000$ DAILY PUBLIC 🔥💸 Real Tournament In Public Channel💸🤑

"
            "🔹100% Accuracy Trades 🤯
"
            "🔹 Personal LOSS Recovery Session 💯
"
            "🔹10-15 Non Mtg Signals 🚀
"
            "🔹Daily Free 90% Working Strategy 📈
"
            "🔹5+ Years of Experience in Binary 📈
"
            "🔹Support 24/7 Assistance📱

"
            "🚀JOIN PUBLIC CHANNEL LINK🔗👇

"
            "🔗https://t.me/+zMqRwLKJVtMyOTVl

"
            "Best regards, ZARA TRADER 📊🏆"
        )
    }
}

def load_users():
    if os.path.exists(USER_DB):
        with open(USER_DB, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_DB, "w") as f:
        json.dump(users, f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user is None:
        return

    user_id = user.id
    first_name = user.first_name
    users = load_users()

    if str(user_id) not in users:
        users[str(user_id)] = True
        save_users(users)

    welcome_text = CHANNELS_BY_LANG["en"]["welcome"].format(name=first_name)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("JOIN FREE VIP💸", url="https://t.me/+zMqRwLKJVtMyOTVl")]
    ])

    await context.bot.send_message(
        chat_id=user_id,
        text=welcome_text,
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN
    )

@app.route("/YOUR_BOT_TOKEN_HERE", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put(update)
    return "OK"

if __name__ == "__main__":
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        webhook_url=f"https://your-project.up.railway.app/{BOT_TOKEN}"
    )
