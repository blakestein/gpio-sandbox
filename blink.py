import RPi.GPIO as GPIO
import time

def blink(pin,pin2,seconds):
	GPIO.output(pin,GPIO.HIGH)
	GPIO.output(pin2,GPIO.LOW)
	time.sleep(seconds)
	GPIO.output(pin,GPIO.LOW)
	GPIO.output(pin2,GPIO.HIGH)
	time.sleep(seconds)
	return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
for i in range(0,50):
	blink(11,15,0.5)

GPIO.cleanup()
