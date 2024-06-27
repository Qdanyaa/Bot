import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    level = logging.INFO
)

tasks = []

num = 0

application = ApplicationBuilder().token("6569412233:AAEyJynHHE6s1t-8m9ofn-nNtSh3-nSQ4OY").build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Hello! I can help you with tracking your tasks.")

async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_of_message = " ".join(context.args)
    status = "Must perform"
    global num
    num += 1
    text = {
        "The text of the message": text_of_message,
        "status": status,
        "ID": num,
    }
    tasks.append(text)
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "The task has been added successfully!✅")

async def get_list_of_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = "\n\n".join("\n".join("{}: {}".format(key, val) for key, val in dictionary.items()) for dictionary in tasks)

    await context.bot.send_message(chat_id = update.effective_chat.id, text = result)

async def mark_as_complete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    num_of_task = tasks[int(context.args[0]) - 1]["ID"]
    print(num_of_task)
    if int(context.args[0]) == num_of_task:
        tasks[num_of_task - 1]["status"] = "Completed"
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "The task has been successfully completed!✅")

if __name__ == "__main__":
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)
    add_task_handler = CommandHandler("add", add_task)
    application.add_handler(add_task_handler)
    list_handler = CommandHandler("list", get_list_of_tasks)
    application.add_handler(list_handler)
    mark_handler = CommandHandler("done", mark_as_complete)
    application.add_handler(mark_handler)
    
    application.run_polling()