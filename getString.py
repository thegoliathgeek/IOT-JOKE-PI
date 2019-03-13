from jokepi import JokePi

ApiKey = ''
Link = 'https://iot-joke-pi.herokuapp.com'

RequestObj = JokePi('String', ApiKey, Link + '/api/request/string/')

d = RequestObj.getString()

print(d)
