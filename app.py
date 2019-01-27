from jokepi import JokePi

# ob = JokePi('Buttons', 'lVTnpCOeT6gcUXRmXdWjXFkn4H53', 'https://nameless-falls-40724.herokuapp.com/api/users/')
ob = JokePi('Buttons', 'lVTnpCOeT6gcUXRmXdWjXFkn4H53', 'http://localhost:3000/api/users/')
updateOb = JokePi('Sensor', 'lVTnpCOeT6gcUXRmXdWjXFkn4H53', 'http://localhost:3000/api/update/')
updateOb.updatePlotData()
# ob.getJsonByIndex()
# ob.testPost()


