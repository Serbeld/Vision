# encoding: utf-8 

# Rubik

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
Se asigna una clase llamada Rubik la cual tendrá métodos de
procesamiento,binarización y ubicación de los colores de un 
objeto.
'''

# NOTA: Es necesario tener conectada una webcam con los drivers de la cámara antes de compilar el código

class Rubik_2_Camaras():


 	def __init__(self,cama):
 		
 		# Asignamos la camara ingresando cv2.VideoCapture(0)
 		# Si quiere asignar una segunda camara externa puede usar cv2.VideoCapture(1)
 		cap = cv2.VideoCapture(cama)
 		self.cap = cap
 		self.cama = cama

 	def captura(self, vector_1, vector_2, dim_del_kernel = 3):


 		#Asignación del rango de los colores en la segmentación
 		color_bajo = np.array(vector_1, dtype=np.uint8)
 		color_alto = np.array(vector_2, dtype=np.uint8)

		# Se toma una Captura de la imagen de la Camara
 		[rec, camara] = self.cap.read()

 		# Se combierten los colores de BGR a HSV (Matíz, Saturación y Brillo)
 		hsv = cv2.cvtColor(camara, cv2.COLOR_BGR2HSV)

 		# Binarización de Color 
 		Mascara = cv2.inRange(hsv, color_bajo, color_alto)

 		# Filtros

 		# Definimos el Kernel
 		kernel = np.ones((dim_del_kernel,dim_del_kernel),np.uint8)
 		# Erosión
 		Mascara = cv2.erode(Mascara,kernel,iterations = 2)
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
 		cv2.imshow('Python'+str(self.cama), Mascara)
 		cv2.imshow('Captura'+str(self.cama), camara)

 		# Se retornan los datos del centroide como salida de este método
 		return(cX,cY)

########################################################################

# Definimos a Cm de clase Rubik por lo que adquiere los métodos antes
# programados...

Cm = Rubik_2_Camaras(0)
Cm2 = Rubik_2_Camaras(1)

# Se crea un ciclo while para hacer captura por captura y 
# tomar la posición del objeto en sus ejes cartesianos (x,y)

while (True):
	

 	# Amarillo:
 	amarillo_bajos = [24,76,72]
 	amarillo_altos = [45, 255, 255]

 	# Azul
 	azul_bajos = [100,40,60]
 	azul_altos = [140, 240, 240]

 	# Rojos:
 	rojo_bajos1 = [0,65,75]
 	rojo_altos1 = [12, 255, 255]

 	rojo_bajos2 = [150,110,110]
 	rojo_altos2 = [255, 255, 255]

 	# Verde:
 	verde_bajos = [49,65,75]
 	verde_altos = [100, 255, 255]

 	[cx,cy] = Cm.captura(azul_bajos,azul_altos,4)
 	[cx2,cy2] = Cm2.captura(azul_bajos,azul_altos,4)

 	print(cx,cy,cx2,cy2)
 	# Sí se pulsa una tecla y la tecla es la letra "q" 
 	# minuscula se rompe el bucle en el que se encuentre

 	if cv2.waitKey(1) & 0xFF == ord('q'):
 		break 

cv2.destroyAllWindows()
#######################################################################