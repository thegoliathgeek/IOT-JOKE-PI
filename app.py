from jokepi import JokePi

#Instance to get JSON
ob = JokePi('Buttons', 'lVTnpCOeT6gcUXRmXdWjXFkn4H53', 'https://nameless-falls-40724.herokuapp.com/api/users/')

#Instance to update Plots
updateOb = JokePi('Sensor', 'lVTnpCOeT6gcUXRmXdWjXFkn4H53', 'https://nameless-falls-40724.herokuapp.com/api/update/')

#Instance to get swtich states
getOb = JokePi('Button', 'lVTnpCOeT6gcUXRmXdWjXFkn4H53', 'https://nameless-falls-40724.herokuapp.com/api/getdata/')


# updateOb.updatePlotData('Sensor 2', '30', '90')

print(getOb.getSwitchState('Shiva'))
