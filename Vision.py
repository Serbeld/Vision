# encoding: utf-8 

# Vision

# Este código va destinado al reconocimiento de objetos 
# por colores mediante la librería open cv en Python...

# Programador Sergio Luis Beleño Díaz
# 08.Enero.2019

'''
Para empezar se importan las librerías de Open cv para visión 
Artificial y se utiliza la librería numpy para la optimización 
de datos al trabajar con las matrices que componen a la imagen 
obtenida pixel por pixel
'''

import cv2
import numpy as np

'''
Se asigna una clase llamada Vision la cual tendrá métodos de
procesamiento,binarización y ubicación de los colores de un 
objeto.
'''

class Vision():


 	def __init__(self):
 		
 		# Asignamos la camara ingresando cv2.VideoCapture(0)
 		cap = cv2.VideoCapture(0)
 		self.cap = cap


 	def captura(self, dim_del_kernel = 3):

		# Se toma una Captura de la imagen de la Camara
 		[rec, camara] = self.cap.read()

 		# Se combierten los colores de BGR a HSV (Matíz, Saturación y Brillo)
 		hsv = cv2.cvtColor(camara, cv2.COLOR_BGR2HSV)

 		# Amarillo:
 		#amarillo_bajos = np.array([24,76,72], dtype=np.uint8)
 		#amarillo_altos = np.array([45, 255, 255], dtype=np.uint8)

 		# Azul
 		azul_bajos = np.array([100,65,75], dtype=np.uint8)
 		azul_altos = np.array([130, 255, 255], dtype=np.uint8)

 		# Rojos:
 		#rojo_bajos1 = np.array([0,65,75], dtype=np.uint8)
 		#rojo_altos1 = np.array([12, 255, 255], dtype=np.uint8)

 		#rojo_bajos2 = np.array([240,65,75], dtype=np.uint8)
 		#rojo_altos2 = np.array([256, 255, 255], dtype=np.uint8)

 		# Verde:
 		#verde_bajos = np.array([49,50,50], dtype=np.uint8)
 		#verde_altos = np.array([100, 255, 210], dtype=np.uint8)


 		# Binarización de Color 
 		Mascara = cv2.inRange(hsv, azul_bajos, azul_altos)

 		# Filtros

 		# Definimos el Kernel
 		kernel = np.ones((dim_del_kernel,dim_del_kernel),np.uint8)
 		# Erosión
 		Mascara = cv2.erode(Mascara,kernel,iterations = 4)
 		# Opening
 		Mascara = cv2.morphologyEx(Mascara, cv2.MORPH_OPEN,kernel)
 		# Closing
 		Mascara = cv2.morphologyEx(Mascara, cv2.MORPH_CLOSE,kernel)
		
 		# Centroide
 		Moments = cv2.moments(Mascara)

 		if (Moments["m00"] != 0):

 			# Se calcula los centroides XY con el fin de ubicar el objeto 

 			cX = int(Moments["m10"] / Moments["m00"])
 			cY = int(Moments["m01"] / Moments["m00"])
 			cv2.circle(camara, (cX, cY), 10, (255, 255, 255), -1)
 			cv2.putText(camara,"Centroide",(cX-60,cY-25),
 				cv2.FONT_HERSHEY_SIMPLEX,1,(255, 255, 255),2)
 		
 		else:
 			cX, cY = 0,0

 		# Muestra las Capturas de la camara en ventanas de visualización
 		cv2.imshow('Python', Mascara)
 		cv2.imshow('Captura', camara)

 		# Se retornan los datos del centroide como salida de este método
 		return(cX,cY)

########################################################################

# Definimos a Cm de clase Vision por lo que adquiere los métodos antes
# programados...

Cm = Vision()

# Se crea un ciclo while para hacer captura por captura y 
# tomar la posición del objeto en sus ejes cartesianos (x,y)

while (True):

	[cx,cy] = Cm.captura()

	print(cx,cy)

	# Sí se pulsa una tecla y la tecla es la letra "q" 
	# minuscula se rompe el bucle en el que se encuentre

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break 

cv2.destroyAllWindows()
#######################################################################