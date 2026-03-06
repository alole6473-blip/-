from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8269173446:AAF-jyU4X3vg0ml_55bykYoqBZMxbpX53TE"
OWNER_ID = 8335918973

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    username = user.username
    text = update.message.text

    msg = f"رسالة جديدة\n\nاليوزر: @{username}\nالايدي: {user.id}\n\nالرسالة:\n{text}"

    await context.bot.send_message(chat_id=OWNER_ID, text=msg)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, forward_message))
app.run_polling()
