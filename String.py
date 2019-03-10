from jokepi import JokePi

ApiKey = ''
Link = 'https://iot-joke-pi.herokuapp.com'

UpdateObj = JokePi('String', ApiKey, Link + '/api/update/string/')

RequestObj = JokePi('String', ApiKey, Link + '/api/request/string/')

k = UpdateObj.updateString('Dazz')

d = RequestObj.getString()

print(d)
