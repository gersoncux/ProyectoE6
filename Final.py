#Librerias de control de Stepper
import sys
import time
import RPi.GPIO as GPIO
#Librerias de Operaciones matematicas
import urllib.request as url
import json
import math 
import time
from cmath import sqrt

#Activacion de Pines
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

aMotorPins = [12, 15, 11, 13]

#Declaracion de Pines
GPIO.setup(16,GPIO.OUT)
servo1=GPIO.PWM(16,50)

for pin in aMotorPins:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin, False)

aSequence = [
	[1,0,0,1],
	[1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1]
]

iNumSteps = len(aSequence)
'''
if sys.argv[3] == "derecha":
	print("d")
else:
	print("")
'''
fWaitTime = 1 / float(1000)

# 1024 pasos son 90 grados
# 4096 pasos son 360 grados

numero0 = 0
guardado = numero0

while True:
	ISS = url.Request("http://api.open-notify.org/iss-now.json")
	response_ISS = url.urlopen(ISS)
	ISS_obj = json.loads(response_ISS.read())
	dato3 = ISS_obj['iss_position']['latitude'];
	dato4 = ISS_obj['iss_position']['longitude'];
	
    #Variables de ISS
	latitud1 = float(14.64072)
	longitud1 = float(-90.51327)
	lat2 = float(dato3)
	lon2 = float(dato4)
	
    #Operacions matematicas
	rad = math.pi/180
	dlat = lat2-latitud1
	dlon = lon2-longitud1
	Rdt = 6372.795477598
	a = math.sin(rad*dlat/2)**2 + math.cos(rad*latitud1)*math.cos(rad*lat2)*math.sin(rad*dlon/2)**2
	distancia = 2*Rdt*math.asin(math.sqrt(a))
	h = 408 #altura de la iss en km
	el = math.atan(h/distancia)
	sube = el*(180/math.pi)
	h = 1228.8
	medida = 2*h*Rdt+h**2
	horizonte = math.sqrt(medida)
	
	#Variables de Stepper
	print("Ingrese los valores")
	grados = int(input("Azimut: "))
	angulo = float(input("Elevacion: "))
	numero0=int(guardado)
	operation = int(grados - numero0)
	posicion=grados
	guardado=posicion 
	iDeg = int(abs(operation)*11.377777777777)
	iSeqPos = 0

	# Calculo del Azimut y de la elevacion
	if(float(dato3) > latitud1 and float(dato4) > longitud1): #Cuadrante I; longitud > -90.51327 ; Latitud > 14.64072------DISTANCIA DE LONGITUD
		dlatI = 0 
		dlonI = lon2-longitud1
		a = math.sin(rad*dlatI/2)**2 + math.cos(rad*latitud1)*math.cos(rad*lat2)*math.sin(rad*dlonI/2)**2 #datos dentro de la raíz
		distanciaI = 2*Rdt*math.asin(math.sqrt(a)) #formula Haversine, distancia de nuestro punto a la proyección del satelite
		azimut = math.acos(distanciaI/distancia)
		giro = azimut*(180/math.pi) 
		turn = round(90-giro,2)
	elif(float(dato3) > latitud1 and float(dato4) < longitud1): #Cuadrante II; longitud > -90.51327 ; Latitud > 14.64072-----DISTANCIA DE LATITUD
		dlatII = lat2-latitud1
		dlonII = 0 
		a = math.sin(rad*dlatII/2)**2 + math.cos(rad*latitud1)*math.cos(rad*latitud1)*math.sin(rad*dlonII/2)**2 #datos dentro de la raíz
		distanciaII = 2*Rdt*math.asin(math.sqrt(a)) #formula Haversine, distancia de nuestro punto a la proyección del satelite
		azimut = math.acos(distanciaII/distancia)
		giro = azimut*(180/math.pi) 
		turn = round(90-giro,2)
	elif(float(dato3) < latitud1 and float(dato4) < longitud1): #Cuadrante III; longitud > -90.51327 ; Latitud > 14.64072-----DISTANCIA DE LONGITUD
		dlatIII = 0 
		dlonIII = lon2-longitud1
		a = math.sin(rad*dlatIII/2)**2 + math.cos(rad*latitud1)*math.cos(rad*latitud1)*math.sin(rad*dlonIII/2)**2 #datos dentro de la raíz
		distanciaIII = 2*Rdt*math.asin(math.sqrt(a)) #formula Haversine, distancia de nuestro punto a la proyección del satelite
		azimut = math.acos(distanciaIII/distancia)
		giro = azimut*(180/math.pi)
		turn = round(90+giro,2)
	elif(float(dato3) < latitud1 and float(dato4) > longitud1): #Cuadrante IV; longitud > -90.51327 ; Latitud > 14.64072------DISTANCIA DE LATITUD
		dlatIV = lat2-latitud1
		dlonIV = 0
		a = math.sin(rad*dlatIV/2)**2 + math.cos(rad*latitud1)*math.cos(rad*lat2)*math.sin(rad*dlonIV/2)**2 #datos dentro de la raíz
		distanciaIV = 2*Rdt*math.asin(math.sqrt(a)) #formula Haversine, distancia de nuestro punto a la proyección del satelite
		azimut = math.acos(distanciaIV/distancia)
		giro = azimut*(180/math.pi)
		turn = round(180-giro,2) 
##################################################################################################################################################################################
	time.sleep(1)
	
	
	
	
	
	#Distancia 1475 distancia maxima en la que se puede captar la ISS	
	if distancia < 20000:
		
		if operation > 0:
			iDirection = -1
			print("derecha")
		elif operation < 0:
			iDirection = 1
			print("izquierda")


		if len(sys.argv) > 4:
			iSeqPos = int(sys.argv[1])


		for step in range(0,iDeg):

			for iPin in range(0, 4):
				iRealPin = aMotorPins[iPin]
				if aSequence[iSeqPos][iPin] != 0:
					GPIO.output(iRealPin, True)
				else:
					GPIO.output(iRealPin, False)

			iSeqPos += iDirection

			if (iSeqPos >= iNumSteps):
				iSeqPos = 0
			if (iSeqPos < 0):
				iSeqPos = iNumSteps + iDirection

			# Tiempo de espera entre cada paso
			time.sleep(fWaitTime)

		for pin in aMotorPins:
			GPIO.output(pin, False)
			
		servo1.start(2.5)
		servo1.ChangeDutyCycle(2.5+(angulo/18))
		time.sleep(1)
		
	else:
		for pin in aMotorPins:
			GPIO.output(pin, False)
			
