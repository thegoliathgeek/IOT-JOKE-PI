from jokepi import JokePi

ApiKey = 'TIORvO9WfJfrjbEEE6gP0BWoha93'
Link = 'https://iotjoke-pi.herokuapp.com'

RequestObj = JokePi('String', ApiKey, Link + '/api/request/string/')

d = RequestObj.getString()

print(d)
