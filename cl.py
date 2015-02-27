import RPi.GPIO as GPIO
import time
import subprocess 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

inc = 0

url = "https://youtube.com/watch?v=wJelEXaPhJ8"

while True:
	if (GPIO.input(7) == True):
		if (inc == 1):
			break
		yt = subprocess.Popen(['youtube-dl', '-g', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
		(res, err) = yt.communicate()
		if res and not err:
			print res
			subprocess.call(['omxplayer', '-o', 'hdmi', '%s' % res.strip()])
			#inc = inc + 1
			#time.sleep(0.5)
			break
GPIO.cleanup()
