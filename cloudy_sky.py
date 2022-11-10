import time
from random import seed
from random import randint
from rpi_ws281x import *

# LED strip configuration:
LED_COUNT      = 64      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 650000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812W_STRIP
A = [0]*LED_COUNT
flag = [1]*LED_COUNT


if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	strip.begin()
	
	seed(1)
	for i in range(LED_COUNT):
		A[i] = randint(0, 255)
		flag[i] = randint(0, 1)
		
	print ('Press Ctrl-C to quit.')
	while True:
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, Color(int(A[i]*0.3), int(A[i]*0.3), A[i]))
			if flag[i] == 1:
				A[i] += randint(0, 1)
			else:
				A[i] -= randint(0, 1)
			if A[i] == 255:
				flag[i] = 0
			if A[i] == 0:
				flag[i] = 1
		print(A[30])
		strip.show()
