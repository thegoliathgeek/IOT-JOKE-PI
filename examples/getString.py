from iotjokepi import JokePi

ApiKey = 'TIORvO9WfJfrjbEEE6gP0BWoha93'
Link = 'https://iotjokepi-pi.herokuapp.com'

RequestObj = JokePi('String', ApiKey, Link + '/api/request/string/')

d = RequestObj.getString()

print(d)
