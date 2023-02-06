import cv2

def tratar(nombre_imagen): 
    # Cargar imagen y verificar que la ruta de la imagen es válida 
    img = cv2.imread(nombre_imagen) 
    # Verificar que la imagen se ha cargado correctamente 
    if img is None:
        raise ValueError("No se pudo cargar la imagen: ", nombre_imagen)
    # Aplicar filtro de diferencia de mediana 
    img_suave = cv2.medianBlur(img, 5) 
    # Convertir a escala de grises 
    img_gris = cv2.cvtColor(img_suave, cv2.COLOR_BGR2GRAY) 
    # Aplicar la diferencia entre la imagen original y la imagen suavizada con el filtro de mediana 
    img_diferencia = cv2.absdiff(img, img_suave) 
    img_gris = cv2.cvtColor(img_diferencia, cv2.COLOR_BGR2GRAY) 
    # Aplicar Canny para detectar los bordes
    img_canny = cv2.Canny(img_gris, 50, 150) 
    # Encontrar contornos 
    contornos, _ = cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    # Verificar que se encontraron al menos un contorno 
    #if len(contornos) == 0:
        #raise ValueError("No se encontraron puntos en la imagen.") 
    # Dibujar los contornos encontrados en la imagen original en rojo 
    img_puntos = img.copy() 
    cv2.drawContours(img_puntos, contornos, -1, (0, 0, 255), 2) 
    # Guardar la imagen con los puntos detectados marcados en rojo 
    cv2.imwrite("img_puntos.jpg", img_puntos) 
    # Imprimir el número de puntos encontrados  
    return len(contornos)/36 