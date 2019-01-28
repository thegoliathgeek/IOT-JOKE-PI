from jokepi import JokePi

ob = JokePi('Buttons', 'lVTnpCOeT6gcUXRmXdWjXFkn4H53', 'https://nameless-falls-40724.herokuapp.com/api/users/')

updateOb = JokePi('Sensor', 'lVTnpCOeT6gcUXRmXdWjXFkn4H53', 'https://nameless-falls-40724.herokuapp.com/api/update/')

getOb = JokePi('Button', 'lVTnpCOeT6gcUXRmXdWjXFkn4H53', 'https://nameless-falls-40724.herokuapp.com/api/getdata/')


# updateOb.updatePlotData('Sensor 2', '30', '90')

getOb.getSwitchState('Sensor 1')