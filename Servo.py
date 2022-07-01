import RPi.GPIO as GPIO
import time
import sys


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)
servo1=GPIO.PWM(16,50)

servo1.start(2.5)
angulo=float(sys.argv[1])
servo1.ChangeDutyCycle(2.5+(angulo/18))
time.sleep(1)

