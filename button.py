import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN) 
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

inc = 0
state = 0

while True:
	if (GPIO.input(7) == True):
		inc = inc + 1
		print inc
		if (inc == 1):
			GPIO.output(11, GPIO.HIGH)
		elif (inc == 2):
			GPIO.output(15, GPIO.HIGH)
		elif (inc == 3):
			GPIO.output(11, GPIO.LOW)
			GPIO.output(15, GPIO.LOW)
			inc = 0
		time.sleep(0.5)
					
GPIO.cleanup()
