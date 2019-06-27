# encoding: utf-8 

# Tomar_Video2_Camaras.py
# Este código va orientado a la toma de imágenes de video mediante la librería open cv en Python...

# Programador Sergio Luis Beleño Díaz
# 27.Junio.2019

# Para empezar se importa la librería de Open cv para visión Artificial

# NOTA: Es necesario tener conectada una webcam con los drivers de la cámara antes de compilar el código

import cv2

# Asignamos la cámara ingresando cv2.VideoCapture(0)
# Si quiere asignar una segunda cámara externa puede usar cv2.VideoCapture(1)
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

while(True):

	# Toma parámetros de captura de la cámara
	[rec, camara] = cap.read()
	[rec2, camara2] = cap2.read()

	# Muestra la imagen tomada en una ventana
	cv2.imshow('Camara1', camara)
	cv2.imshow('Camara2', camara2)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
