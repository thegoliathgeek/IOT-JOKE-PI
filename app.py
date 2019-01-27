from jokepi import JokePi

ob = JokePi('Buttons', 'lVTnpCOeT6gcUXRmXdWjXFkn4H53', 'https://nameless-falls-40724.herokuapp.com/api/users/')

updateOb = JokePi('Sensor', 'lVTnpCOeT6gcUXRmXdWjXFkn4H53', 'https://nameless-falls-40724.herokuapp.com/api/update/')

# updatePlotData(Plot-Name, X-axis Value , Y-axis Value)
updateOb.updatePlotData('Sensor', '100', '500')
