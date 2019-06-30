# encoding: utf-8 

# MyHand

# Este código va destinado al reconocimiento del movimiento 
# de un brazo robótico mediante la librería open cv en Python...

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
cap = cv2.VideoCapture(0)

#########################################################################
#########################################################################
# funtion

import math

def dist(x1,y1,x2,y2):
	raiz = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
	return(raiz)


def filtro(Mascara, dim_del_kernel = 3,iteraciones_de_la_erosion = 2):

	# Kernel
 	kernel = np.ones((dim_del_kernel,dim_del_kernel),np.uint8)
 	# Erosión
 	Filtro_Mascara = cv2.erode(Mascara,kernel,iterations = iteraciones_de_la_erosion)
 	# Opening
 	Filtro_Mascara = cv2.morphologyEx(Filtro_Mascara, cv2.MORPH_OPEN,kernel)
 	# Closing
 	#Filtro_Mascara = cv2.morphologyEx(Filtro_Mascara, cv2.MORPH_CLOSE,kernel)
 	return Filtro_Mascara


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


def captura(colorhsv_bajo = [0,0,0], colorhsv_alto = [255,200,90],
	colorhsv_bajo1 = [100,65,75], colorhsv_alto1 = [130, 255, 255],
	colorhsv_bajo2 = [49,50,50], colorhsv_alto2 = [100, 255, 210]):

	# Se toma una Captura de la imagen de la Camara
 	[rec, camara] = cap.read()
 	camara = cv2.resize(camara, (840,640))

 	# Se combierten los colores de BGR a HSV (Matíz, Saturación y Brillo)
 	hsv = cv2.cvtColor(camara, cv2.COLOR_BGR2HSV)

 	# Colores:
 	
 	bajos = np.array(colorhsv_bajo, dtype=np.uint8)
 	altos = np.array(colorhsv_alto, dtype=np.uint8)

 	bajos1 = np.array(colorhsv_bajo1, dtype=np.uint8)
 	altos1 = np.array(colorhsv_alto1, dtype=np.uint8)

 	bajos2 = np.array(colorhsv_bajo2, dtype=np.uint8)
 	altos2 = np.array(colorhsv_alto2, dtype=np.uint8)


 	# Binarización de Color 
 	img_binarizada_1 = cv2.inRange(hsv, bajos, altos)
 	img_binarizada_2 = cv2.inRange(hsv, bajos1, altos1)
 	img_binarizada_3 = cv2.inRange(hsv, bajos2, altos2)

#################################################################
#################################################################

 	# Filtros

 	# Mascara
 	img_binarizada_1 = filtro(img_binarizada_1)
 	# Mascara1
 	img_binarizada_2 = filtro(img_binarizada_2)
 	# Mascara2
 	img_binarizada_3 = filtro(img_binarizada_3)

#######################################################################
#######################################################################

 	# Centroides
 	[hombrox, hombroy] = centroide(img_binarizada_1)
 	[codox, codoy] = centroide(img_binarizada_2)
 	[manox, manoy] = centroide(img_binarizada_3)

###############################################################################
###############################################################################

 	# Dibujos

 	# Configuración inicial
 	cv2.line(camara,(hombrox , hombroy + 60),(hombrox, hombroy - 60),(255, 0, 0),20)
 	cv2.line(camara,(hombrox , hombroy + 60),(hombrox - 60, hombroy + 60),(255, 0, 0),20)
 	cv2.line(camara,(hombrox , hombroy - 60),(hombrox - 60, hombroy - 60),(255, 0, 0),20)

 	# Antebrazo
 	cv2.line(camara,( codox , codoy),(manox, manoy),(255, 0, 0),30)
 	# Bíceps
 	cv2.line(camara,(hombrox, hombroy),(codox, codoy),(255, 0, 0),30)
 	# Hombro
 	cv2.circle(camara,(hombrox, hombroy),40,(0, 255, 0),-1)
 	# Codo
 	cv2.circle(camara,(codox, codoy),40,(0, 255, 0),-1)
 	# Mano
 	cv2.circle(camara,(manox, manoy),40,(0, 255, 0),-1)


#########################################################################
#########################################################################
	# Cálculo

	#dist(x1,y1,x2,y2)
	tronco = dist(hombrox, hombroy, hombrox, codoy)
	bicep = dist(hombrox, hombroy, codox, codoy)
	ante_brazo = dist(codox, codoy, manox, manoy)
	#angulo1 = math.degrees(1/(math.cos(tronco/bicep)))
	#angulo2 = math.degrees(1/(math.cos(cateto_abyacente/hipotenusa)))
	
	print("Bicep "+str(int(bicep))+(", ")+"Ante_brazo "+str(int(ante_brazo)))
#########################################################################

 	# Muestra las Capturas de la camara en ventanas de visualización
 	cv2.imshow('Camara', camara)

#########################################################################
#########################################################################

# Se crea un ciclo while para hacer captura por captura y 
# tomar la posición del objeto en sus ejes cartesianos (x,y)


while (True):
	
	# Negro:
	#nbajo = [0,0,0]
	#nalto = [255,200,90]

	# Verde:
	#gbajo = [49,50,50]
	#galto = [100, 255, 210]

	# Azul:
	#bbajo = [100,65,75]
	#balto = [130, 255, 255]

 	# Amarillo:
 	#abajos = [24,76,72]
 	#aaltos = [45, 255, 255]

	# Captura(ValorHSVbajo,ValorHSValto)
	captura()

	# Sí se pulsa una tecla y la tecla es la letra "q" 
	# minuscula se rompe el bucle en el que se encuentre

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break 

cv2.destroyAllWindows()

#######################################################################
#######################################################################