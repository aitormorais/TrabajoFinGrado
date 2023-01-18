import telegram
from telegram import Update,KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import threading
import requests
latitud,longitud=181,181
ubicacion = False
def process_image(path):

    print("Processing image")

    ##### Process the image and detct dots here #####
    print("introducidas:",latitud,longitud)
    placeholder_data = {
        "nombre":"Deusto",
        "lat": latitud, 
        "lng": longitud,
    }

    requests.post("http://127.0.0.1:8000/api/data/", json=placeholder_data)

async def message_handler(update: Update, context):
    #print("pedimos:")
    #lat,lng=location_handler(update,context)
    # Check if there is any image attached
    global ubicacion
    if update.message.location:
        location = update.message.location
        global latitud 
        latitud = location.latitude
        global longitud 
        longitud = location.longitude
        ubicacion = True
        print("Imprimimos valores: ",latitud,longitud)

    if update.message.photo and ubicacion:
        print("Photo attached")
        # Get the file id of the image
        file_id = update.message.photo[-1].file_id
        # Get the file from the file id
        file = await context.bot.get_file(file_id)
        # Download and save the file
        file_url = f'https://api.telegram.org/file/bot{"5872441848:AAGuR3ed2YfBNjgD_OvBKERHxHO9sWhsG14"}/{file.file_path}'
        response = requests.get(file_url)
        open("image.jpg", "wb").write(response.content)
        #location_handler(update,context)
        #await file.download("image.jpg")
        #keyboard = [[telegram.KeyboardButton("Enviar mi ubicación", request_location=True)]]
        #reply_markup = telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        #await update.message.reply_text("Image received. Please share your location.", reply_markup=reply_markup)
        # Send a message to the user
        t = threading.Thread(target=process_image, args=("image.jpg",))
        t.start()
        await update.message.reply_text("Image received. Processing...")
        # Process the image in a new thread
        
        
    else:
        await update.message.reply_text("No image attached")

app = ApplicationBuilder().token("5872441848:AAGuR3ed2YfBNjgD_OvBKERHxHO9sWhsG14").build()

#app.add_handler(CommandHandler("prompt", prompt))
#app.bot.send_message(chat_id,"Por favor primero ingresar ubicacion y despues foto...")
app.add_handler(MessageHandler(filters=None, callback=message_handler))
app.run_polling()
