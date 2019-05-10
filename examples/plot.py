from iotjokepi import JokePi

ApiKey = 'Your API Key'
Link = 'http://iot-joke-pi.herokuapp.com'

# Instance to update Plots
updateOb = JokePi('Sensor', ApiKey, Link + '/api/update/')


updateOb.updatePlotData('Plot Name', '30', '90')

