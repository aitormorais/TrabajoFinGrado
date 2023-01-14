from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import threading
import requests

def process_image(path):

    print("Processing image")

    ##### Process the image and detct dots here #####

    placeholder_data = {
        "nombre":"Deusto",
        "lat": "43.2730147", 
        "lng": "-2.9559029",
    }

    requests.post("http://127.0.0.1:8000/api/data/", json=placeholder_data)

async def message_handler(update: Update, context):
    # Check if there is any image attached
    if update.message.photo:
        print("Photo attached")
        # Get the file id of the image
        file_id = update.message.photo[-1].file_id
        # Get the file from the file id
        file = await context.bot.get_file(file_id)
        # Download and save the file
        file_url = f'https://api.telegram.org/file/bot{"5872441848:AAGuR3ed2YfBNjgD_OvBKERHxHO9sWhsG14"}/{file.file_path}'
        response = requests.get(file_url)
        open("image.jpg", "wb").write(response.content)
        #await file.download("image.jpg")
        # Send a message to the user
        t = threading.Thread(target=process_image, args=("image.jpg",))
        t.start()
        await update.message.reply_text("Image received. Processing...")
        # Process the image in a new thread
        
        
    else:
        await update.message.reply_text("No image attached")

app = ApplicationBuilder().token("5872441848:AAGuR3ed2YfBNjgD_OvBKERHxHO9sWhsG14").build()

#app.add_handler(CommandHandler("prompt", prompt))
app.add_handler(MessageHandler(filters=None, callback=message_handler))
app.run_polling()