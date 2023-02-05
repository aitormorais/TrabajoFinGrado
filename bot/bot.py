import telegram
from PIL import Image
from telegram import Update,KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import threading
import requests
import os
import asyncio
import logging
import aiohttp
import urllib
import json
import re 
import tratar_imagen as t_img
logging.basicConfig(level=logging.ERROR)
latitud,longitud=0,0
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
async def process_image(update, context):
    try:
        logging.info("Procesando imagen")
        contamina = t_img.tratar("a.jpg")
        print("COTAMIACIODTCTADA: ",contamina)
        print("introducidas:",latitud,longitud)
        peticion = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key=AIzaSyAk-jcafbBJsvLF2MnZS9m0wOgQCDi4mCs".format(latitud,longitud)
        response = requests.get(peticion)
        if response.status_code == 200:
            online = response.json()
            json_data = json.dumps(online)
            print(type(json_data))
            data = response.json()
            # Guarda el JSON en un archivo
            with open("data.json", "w") as outfile:
                json.dump(data, outfile)
            with open('data.json', 'r') as file:
                data = json.load(file)
            r = data['results']
            texto =str(r[0])
            result = re.search(r"'formatted_address': '(.*?)'", texto)
            nombre = ""
            if result:
                nombre = result.group(1)
            else:
                nombre = "ubicacion desconocida"
            
        else:
            print("La petición GET falló con el código de estado:", response.status_code)
        placeholder_data = {
            "nombre":nombre,
            "lat": latitud, 
            "lng": longitud,
            "contaminacion":contamina,
        }
        requests.post("http://127.0.0.1:8000/api/data/", json=placeholder_data)
        await asyncio.sleep(1)
    except Exception as e:
        logging.error(f"Ha ocurrido un error: {e}")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Lo siento, ha ocurrido un error inesperado. Por favor, inténtalo de nuevo más tarde.")
async def message_handler(update: Update, context):
    if update.message.location:
        location = update.message.location
        global latitud 
        latitud = location.latitude
        global longitud 
        longitud = location.longitude

    if update.message.photo:

        file_id = update.message.photo[-1].file_id
        foto = await context.bot.get_file(file_id)
        response = requests.get(foto.file_path)
        with open('a.jpg', 'wb') as f:
            f.write(response.content)
        await update.message.reply_text("Image received. Processing...")
        await process_image(Update, context)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Gracias, hemos procesado su imagen.")     
  
    else:
        await update.message.reply_text("No image attached")

app = ApplicationBuilder().token("5872441848:AAGuR3ed2YfBNjgD_OvBKERHxHO9sWhsG14").build()
app.add_handler(MessageHandler(filters=None, callback=message_handler))
app.run_polling()