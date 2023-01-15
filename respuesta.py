#Para contar los puntos en cada cuadrícula utilizando la escala de DUSTCH (Densely Under-sampled STructures with CHaracteristics), puedes seguir los siguientes pasos:

#Convertir la imagen a escala de grises: Utilizando la función cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) de OpenCV, conviertes la imagen a escala de grises.
#Aplicar un filtro gaussiano: Utilizando la función cv2.GaussianBlur() de OpenCV, aplicas un filtro gaussiano para suavizar la imagen y reducir el ruido.
#Aplicar una operación morfologica: Utilizando la función cv2.morphologyEx() de OpenCV, aplicas una operación morfológica para eliminar las estructuras pequeñas y suavizar las estructuras grandes.
#Aplicar una transformación de gradiente: Utilizando la función cv2.morphologyEx() de OpenCV, aplicas una transformación de gradiente para resaltar las estructuras de la imagen.
#Umbralizar la imagen: Utilizando la función cv2.threshold() de OpenCV, umbralizas la imagen para convertirla en una imagen binaria.
#Encuentra los contornos: Utilizando la función cv2.findContours() de OpenCV, encuentras los contornos de la imagen binaria.
#Contar los puntos: Recorres los contornos encontrados y cuentas los puntos que se encuentran dentro de cada cuadrícula.
#Es importante mencionar que el proceso de contar los puntos con la escala de DUSTCH requiere de un ajuste fino de los parámetros de los filtros y operaciones morfologicas, para lograr un mej

import cv2

img = cv2.imread("imagen.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Aplicar un filtro gaussiano
#En este caso, se establece el tamaño del kernel en (5,5) 
#para el filtro gaussiano y se utiliza un valor de sigma de 0.
# Estos valores pueden ser ajustados según las necesidades del usuario.
# Luego se guarda la imagen con el filtro aplicado con el nombre "imagen_gaussiana.jpg"
kernel_size = (5,5)
gray_blur = cv2.GaussianBlur(gray, kernel_size, 0)

#Aplicar operación morfológica
#En este caso, se utiliza un elemento estructurante de tipo rectángulo de tamaño (3,3) y se utiliza la operación MORPH_OPEN. 
#La operación MORPH_OPEN suaviza las estructuras grandes y elimina las estructuras pequeñas.
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
gray_morfo = cv2.morphologyEx(gray_blur, cv2.MORPH_OPEN, kernel)

#Aplicar transformación de gradiente para resaltar las estructuras de la imagen.
gray_gradient = cv2.morphologyEx(gray_morfo, cv2.MORPH_GRADIENT, kernel)

# Umbralizar la imagen
_, threshold = cv2.threshold(gray_gradient, 100, 255, cv2.THRESH_BINARY)

# Buscar contornos
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Contar puntos
puntos = 0
for contour in contours:
    puntos += len(contour)

print("Se encontraron ", puntos, " puntos en la imagen.")

cv2.imwrite("imagennn.jpg", threshold )
