import RPi.GPIO as gp
import time


gp.setmode(gp.BOARD)
inPin=3
gp.setup(inPin,gp.IN)

while True:
	if gp.input(inPin) == 1:
		print('Touched')
	else:
		print('Untouched')
