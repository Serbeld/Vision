# encoding: utf-8 

# Tomar_Video.py
# Este código va orientado a la toma de imágenes de video mediante la librería open cv en Python...

# Programador Sergio Luis Beleño Díaz
# 05.Junio.2019

#Para empezar se importa la librería de Open cv para visión Artificial

import cv2

# Asignamos la cámara ingresando cv2.VideoCapture(0)
# Si quiere asignar una segunda cámara externa puede usar cv2.VideoCapture(1)
cap = cv2.VideoCapture(0)

while(True):

	# Toma parámetros de captura de la cámara
	[rec, camara] = cap.read()

	# Muestra la imagen tomada en una ventana
	cv2.imshow('Nombre de la ventana de video', camara)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()