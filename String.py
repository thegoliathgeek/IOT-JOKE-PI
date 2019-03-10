from jokepi import JokePi

ApiKey = ''
Link = 'https://iot-joke-pi.herokuapp.com'

obj = JokePi('String', ApiKey, Link + '/api/update/string/')

k = obj.updateString('Dazz')


print(k)
