import telegram
from telegram import Update,KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import threading
import requests
import cv2
latitud,longitud=0,0
def suavizar(nombre_imagen):
    # Cargar imagen
  img = cv2.imread(nombre_imagen)

  # Aplicar filtro de diferencia de mediana
  img_suave = cv2.medianBlur(img, 5)

  # Convertir a escala de grises
  img_gris = cv2.cvtColor(img_suave, cv2.COLOR_BGR2GRAY)

  # Aplicar la diferencia entre la imagen original y la imagen suavizada con el filtro de mediana
  img_diferencia = cv2.absdiff(img, img_suave)
  resultado = "resultado.jpg"
  # Guardar la imagen con las manchas resaltadas
  cv2.imwrite(resultado, img_diferencia)

def contar(nombre):
    # Cargar imagen con las manchas resaltadas
  img = cv2.imread(nombre)

  # Convertir a escala de grises
  img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # Aplicar threshold binario para eliminar el ruido
  _, img_thresh = cv2.threshold(img_gris, 50, 255, cv2.THRESH_BINARY)

  # Encontrar contornos
  contornos, _ = cv2.findContours(img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Dibujar los contornos encontrados en la imagen original en rojo
  img_puntos = img.copy()
  cv2.drawContours(img_puntos, contornos, -1, (0, 0, 255), 2)

  # Guardar la imagen con los puntos detectados marcados en rojo
  cv2.imwrite("imagen_puntos.jpg", img_puntos)

  # Imprimir el número de puntos encontrados
  print("Número de puntos encontrados: ", len(contornos))
  result = len(contornos)/36

  return str(result)
def process_image(path):

    print("Processing image")

    ##### Detectar puntos aqui #####
    suavizar("prueba.jpg")
    contamina= contar("resultado.jpg")

    print("introducidas:",latitud,longitud)
    placeholder_data = {
        "nombre":"Deusto",
        "lat": latitud, 
        "lng": longitud,
        "contaminacion":contamina,
    }

    requests.post("http://127.0.0.1:8000/api/data/", json=placeholder_data)

async def message_handler(update: Update, context):
    #print("pedimos:")
    #lat,lng=location_handler(update,context)

    if update.message.location:
        location = update.message.location
        global latitud 
        latitud = location.latitude
        global longitud 
        longitud = location.longitude
        print("Imprimimos valores: ",latitud,longitud)

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
app.add_handler(MessageHandler(filters=None, callback=message_handler))
app.run_polling()
