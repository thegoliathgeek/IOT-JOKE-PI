IOT JOKE PI
===============

This is a python library to access iot website
 IOT-JOKE(https://iot-joker.firebaseapp.com)

Functions:
----------
* Control devices using switches
* Plot your sensor data

Installation :
--------------

Python3
-------

::

    pip3 install pyiotjoke

or

::

    pip install pyiotjoke


**Implementing :**
~~~~~~~~~~~~~~~~~~

::

    from iotjokepi import JokePi

    ApiKey = 'Your API Key'
    Link = 'http://iot-joke-pi.herokuapp.com'

    # Instance to get swtich states
    getOb = JokePi('Button', ApiKey, Link + '/api/getdata/')


    data1 = getOb.getSwitchState('Switch Name')
    data = data1

    if data == 'ON':
        print('Switch is ON')
    elif data == 'OFF':
        print('Switch is OFF')
    else:
        print('Invalid Device')

