import RPi.GPIO as GPIO
import time

button = 7
light1 = 11
light2 = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(light1, GPIO.OUT)
GPIO.setup(light2, GPIO.OUT)

def light(state):
	inc = state	
	try:
		GPIO.wait_for_edge(button, GPIO.FALLING)
		inc += 1
		print inc
		if (inc == 1):
			GPIO.output(light1, GPIO.HIGH)
		elif (inc == 2):
			GPIO.output(light2, GPIO.HIGH)
		elif (inc == 3):
			GPIO.output(light1, GPIO.LOW)
			GPIO.output(light2, GPIO.LOW)
		time.sleep(0.2)
					
	except KeyboardInterrupt:
		GPIO.cleanup()
	if (inc < 3):
		light(inc)
	else:
		light(0)
light(0)
GPIO.cleanup()
