import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

aMotorPins = [12, 15, 11, 13]

#Declaracion de Pines
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


fWaitTime = 1 / float(1000)

# 1024 pasos son 90 grados
# 4096 pasos son 360 grados

grados = int(input("Azimut: "))
iDeg = int(abs(grados)* 11.377777777777)
iSeqPos = 0

iSeqPos = 0

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
			

		
else:
	for pin in aMotorPins:
		GPIO.output(pin, False)


