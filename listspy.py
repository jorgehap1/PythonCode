planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])
print(' ')
##Modificar valores de la lista
planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

##longitud de una lista len()
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

## Agregar valores a la lista .append(value)

planets.append("Pluto") # lo deja en el ultimo registro

## Eliminar .pop()

planets.pop()  # Goodbye, Pluto se elimina el ultimo elemento

######### Indices Negativos ###
""" Los índices negativos comienzan al final de la lista y van hacia atrás."""

print("The last planet is", planets[-1]) # Ultimo elemento de la lista
print("The penultimate planet is", planets[-2]) # penultimo elemento de la lista

####### Busqueda de un valor ###
"""  para buscar use index, si no encuentra devuelve -1"""
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun") # se ingrementa para mostrar el numero correcto

#### Numeros

gravity_on_earth = 1.0
gravity_on_the_moon = 0.166

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]


bus_weight = 12650 #KG on Earth
print('On mercury, a double-decker bus weight', bus_weight*gravity_on_planets[0], "KG")


##  Uso de min() y max() con listas

print("The lightest a bus would be in the solar system is ",bus_weight* min(gravity_on_planets),"Kg")
print("The heaviest a bus would be in the solar system is ", bus_weight*max(gravity_on_planets), "Kg")

#### Segmentacion de listas
planets_before_earth = planets[0:2] # no se incluye el elemnto que termina en este caso 2 tierra
print(planets_before_earth)

planets_after_earth = planets[3:] ## si no tiene indice se asume que va hasta el final 
print(planets_after_earth)

### Combincion de listas
""" Para unir dos listas, debe usar el otro operador (+) con dos listas para devolver una nueva. """

amalthea_group = ["Metis","Adrastea","Amalthea","Thebe"]
galilean_moons = ["IO","Europa","Ganymede","Callisto"]
regular_satellite_moons =amalthea_group +galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

### Ordenar listas .sort() alfabeticamente o orden numerico
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort(reverse=True) ##ordena inverso

print(" ")

#####################
####### EJERCICIO ###

user_planet = input("Please enter the name of the planet (with a capital letter to start)")
planet_index = planets.index(user_planet)
print("Here are the planets closer than ", user_planet)
print(planets[0:planet_index])






