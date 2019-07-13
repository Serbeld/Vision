# encoding: utf-8

# Duke the dog

# Este código va destinado al reconocimiento de un perro por su color de pelaje,
# eliminando todo ruido causado por el ambiente.
# Todo mediante la librería open cv en Python..subl

# Programador Sergio Luis Beleño Díaz
# Enero.2019

'''
Para empezar se importan las librerías de Open cv para visión
Artificial y se utiliza la librería numpy para la optimización
de datos al trabajar con las matrices que componen a la imagen
obtenida pixel por pixel
'''

import cv2
import numpy as np

# Asignamos la camara ingresando cv2.VideoCapture(0)
cap = cv2.VideoCapture('Duke the dog.mp4')

# funtion

def centroide(imagen_binarizada):
	
	# Obtenemos lo momentos de la imagen
	Moments = cv2.moments(imagen_binarizada)

	if (Moments["m00"] != 0):

 		# Se calcula los centroides XY con el fin de ubicar el objeto

 		centrox = int(Moments["m10"] / Moments["m00"])
 		centroy = int(Moments["m01"] / Moments["m00"])
 		
	else:
 		centrox, centroy = 0,0

	return(centrox, centroy)

def captura(colorrgb_bajo = [175,100,60], colorrgb_alto = [195,115,75]):

	#(colorrgb_bajo = [165,40,11], colorrgb_alto = [195,115,100]):
	# Se toma una Captura de la imagen de la Camara
 	[rec, camara] = cap.read()
 	
 	if rec == True:

 		camara = cv2.resize(camara, (1040,680))

 		# Se combierten los colores de BGR a rgb (Rojo, Verde y Azul)
 		rgb = cv2.cvtColor(camara, cv2.COLOR_BGR2RGB)

 		# Colores:
 		bajos = np.array(colorrgb_bajo, dtype=np.uint8)
 		altos = np.array(colorrgb_alto, dtype=np.uint8)

 		# Binarización de Color
 		img_binarizada = cv2.inRange(rgb, bajos, altos)

 		# Filtros


 		# Centroides
 		[x, y] = centroide(img_binarizada)

 		try: x2
 		except NameError: i = None

 		if (i == None):
 			x2 = x
 			y2 = y
 		
 		x = (x + x2)/2
 		y = (y + y2)/2
 		x2 = x
 		y2 = y
 			
 		cv2.line(camara,(x-100 , y-50),(x+100, y-50),(75, 255, 50),15)
 		cv2.line(camara,(x+100 , y-50),(x+100, y+150),(75, 255, 50),15)
 		cv2.line(camara,(x-100 , y-50),(x-100, y+150),(75, 255, 50),15)
 		cv2.line(camara,(x-100 , y+150),(x+100, y+150),(75, 255, 50),15)
 		cv2.putText(camara,"Duke the dog",(x-100,y+200),cv2.FONT_HERSHEY_DUPLEX,1,(75, 255, 50),2)


 		print(x,y)

		# Muestra las Capturas de la camara en ventanas de visualización
 		#cv2.imshow('Mascara', img_binarizada)
 		cv2.imshow('Camara', camara)
 		
 		return 1


 	else:
 		return 0

#########################################################################

# Se crea un ciclo while para hacer captura por captura y
# tomar la posición del objeto en sus ejes cartesianos (x,y)


while (cap.isOpened()):

	# Captura(ValorHSVbajo,ValorHSValto)
	cond = captura()

	# Sí se pulsa una tecla y la tecla es la letra "q"
	# minuscula se rompe el bucle en el que se encuentre

	if cv2.waitKey(15) & 0xFF == ord('q') or cond == 0:
		break

cap.release()
cv2.destroyAllWindows()