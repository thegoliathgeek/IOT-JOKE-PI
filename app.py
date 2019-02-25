from jokepi import JokePi

ApiKey = 'MCv0RZ5tzNOHbQBobpZ6aqUIDbP2'
Link = 'https://iot-joke-pi.herokuapp.com'
# Instance to get JSON
ob = JokePi('Buttons', ApiKey, Link + '/api/users/')

# Instance to update Plots
updateOb = JokePi('Sensor', ApiKey, Link + '/api/update/')

# Instance to get swtich states
getOb = JokePi('Button', ApiKey, Link + '/api/getdata/')

# updateOb.updatePlotData('Sensor 2', '30', '90')

data = getOb.getSwitchState('Fann')

# data = updateOb.updatePlotData('dazz','10','20')

if data == 'ON':
    print('Fan is ON')
elif data == 'OFF':
    print('Fan is OFF')
else:
    print('Invalid Device')
