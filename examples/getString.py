from iotjokepi import JokePi

ApiKey = 'Your API Key'
Link = 'https://iot-joke-pi.herokuapp.com'

RequestObj = JokePi('String', ApiKey, Link + '/api/request/string/')

d = RequestObj.getString()

print(d)
