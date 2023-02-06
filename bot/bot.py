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
import logging
latitud,longitud=0,0
logging.basicConfig(level=logging.ERROR, filename='errors.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.basicConfig(level=logging.DEBUG, filename='debug.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
async def process_image(update, context):
    try:
        logging.debug("Procesando imagen")
        contamina = t_img.tratar("a.jpg")
        peticion = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key=AIzaSyAk-jcafbBJsvLF2MnZS9m0wOgQCDi4mCs".format(latitud,longitud)
        response = requests.get(peticion)
        if response.status_code == 200:
            online = response.json()
            json_data = json.dumps(online)
            data = response.json()
            with open("data.json", "w") as file:
                json.dump(data, file)
            with open('data.json', 'r') as file:
                data = json.load(file)
            r = data['results']
            if r:
                texto = str(r[0])
                result = re.search(r"'formatted_address': '(.*?)'", texto)
                nombre = ""
                if result:
                    nombre = result.group(1)
                else:
                    nombre = "ubicacion desconocida"
            else:
                nombre = "ubicacion desconocida"
        else:
            logging.error(f"La petición GET falló con el código de estado: {response.status_code}")
            await update.message.reply_text("No se pudo obtener la ubicación.")
            return
        placeholder_data = {
            "nombre":nombre,
            "lat": latitud, 
            "lng": longitud,
            "contaminacion":contamina,
        }
        if latitud == 0 and longitud == 0:
            await update.message.reply_text("Por favor, envía tus coordenadas antes de enviar la imagen.")
            return
        requests.post("http://127.0.0.1:8000/api/data/", json=placeholder_data)
        await asyncio.sleep(1)
    except Exception as e:
        logging.error(f"Ha ocurrido un error: {e}")
        await update.message.reply_text("Lo siento, ha ocurrido un error inesperado. Por favor, inténtalo de nuevo más tarde...")
async def message_handler(update: Update, context):
    try:
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
            await update.message.reply_text("Imagen recibida, Procesando...")
            await process_image(Update, context)
            await update.message.reply_text("Gracias, hemos procesado su imagen.")   
        else:
            await update.message.reply_text("No se a subido imagen")
    except Exception as e:
        logging.error(f"Ha ocurrido un error en message_handler: {e}")
        await update.message.reply_text("Lo siento, ha ocurrido un error inesperado. Por favor, inténtalo de nuevo más tarde...")
app = ApplicationBuilder().token("5872441848:AAHbEuKjbPJSzy8dUBLUw4P8r3WDiITqX1A").build()
app.add_handler(MessageHandler(filters=None, callback=message_handler))
app.run_polling()