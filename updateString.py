
from jokepi import JokePi

ApiKey = 'TIORvO9WfJfrjbEEE6gP0BWoha93'
Link = 'https://iot-joke-pi.herokuapp.com'


UpdateObj = JokePi('String', ApiKey, Link + '/api/update/string/')

k = UpdateObj.updateString('Dazz')

print(k)
