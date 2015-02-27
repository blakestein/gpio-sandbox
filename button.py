import RPi.GPIO as GPIO
import time

button = 7
light1 = 11
light2 = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(button, GPIO.IN) 
GPIO.setup(light1, GPIO.OUT)
GPIO.setup(light2, GPIO.OUT)

inc = 0
state = 0

while True:
	if (GPIO.input(button) == True):
		inc = inc + 1

		if (inc == 1):
			GPIO.output(light1, GPIO.HIGH)
		elif (inc == 2):
			GPIO.output(light2, GPIO.HIGH)
		elif (inc == 3):
			GPIO.output(light1, GPIO.LOW)
			GPIO.output(light2, GPIO.LOW)
			break	
		time.sleep(0.5)
					
GPIO.cleanup()
