from jokepi import JokePi
import RPi.GPIO as gp
import time
ledPin=5
userId=''

gp.setmode(gp.BOARD)

gp.setup(ledPin,gp.OUT)

switchName=''

getOb = JokePi('Button', '', 'https://nameless-falls-40724.herokuapp.com/api/getdata/')

state = 'OFF'
prev = 'OFF'

while True:
	state = getOb.getSwitchState(switchName)
	if prev != state:
		prev = state
	if prev == 'ON':
		print(state)
		gp.output(ledPin,gp.HIGH)
	else:
		print(state)
		gp.output(ledPin,gp.LOW)
