#Librerias de control de Stepper
import sys
import time
import RPi.GPIO as GPIO
#Librerias de Operaciones matematicas
import urllib.request as url
import json
import math 
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
'''
referencia = 0
save = referencia
'''

while True:
	
	ISS = url.Request("http://api.open-notify.org/iss-now.json")
	response_ISS = url.urlopen(ISS)
	ISS_obj = json.loads(response_ISS.read())
	dato3 = ISS_obj['iss_position']['latitude'];
	dato4 = ISS_obj['iss_position']['longitude'];
	
    #Variables de ISS
	lat1 = float(14.64072)
	lon1 = float(-90.51327)
	lat2 = float(dato3)
	lon2 = float(dato4)
	
    #Operacions matematicas
	rad = math.pi/180
	dlat = lat2-lat1
	dlon = lon2-lon1
	r = 6372.795477598
	a = math.sin(rad*dlat/2)**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*math.sin(rad*dlon/2)**2
	distancia = 2*r*math.asin(math.sqrt(a))
	print("la distancia es de ",distancia," Km")
	
	#Variables de Stepper
	#referencia = save
	grados = int(input("Azimut: "))
	#operation = grados - referencia
	#print("valor: ", operation)
	#save = operation
	angulo = float(input("Elevacion: "))
	iDeg = int(abs(grados)* 11.377777777777)
	iSeqPos = 0

	
	#Distancia 1475 distancia maxima en la que se puede captar la ISS
	if distancia < 16075:
		
		if grados > 0:
			iDirection = 1
			print("derecha")
		elif grados < 0:
			iDirection = -1
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
			
