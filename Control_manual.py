import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Declaracion de variables

pin1 = 12
pin2 = 15
pin3 = 11
pin4 = 13


#Declaracion de pines

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)
WaitTime = 0.001

def derecha():
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.LOW)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.LOW)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.LOW)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.LOW)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.LOW)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(WaitTime)

def izquierda():
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.LOW)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.LOW)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.LOW)
	time.sleep(WaitTime)

def reposo():
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.LOW)
	
	

while True:
	grados = int(input("ingrese cantidad en Grados:"))
	distancia = int(input("ingrese distancia: "))
	pasos = int(abs(grados)*1.422222222)	
	numero_pasos = 0
	
	if distancia < 1200:		
		while grados > numero_pasos:
			izquierda()
			numero_pasos = numero_pasos + 1
				
		while grados < numero_pasos:
			derecha()
			numero_pasos = numero_pasos + 1
	else:
		reposo()
