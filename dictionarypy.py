planet = {
    'name': 'Earth',
    'moons': 1
}
## get para obtener el valor con el nombre de clave, si la clave no eta disponibñe devuelve NONE
print(planet.get('name'))
# otra forma mas comun, genera error sino esta disponible
print(planet['name'])


### Modificar valores de diccionario .update
planet.update({'name': 'Makemake'})
# otra forma 
planet['name'] = 'Makemake'



# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79

################# Adicion y eliminacion de claves 
planet['orbital period'] = 4333
# Eliminar con pop
planet.pop('orbital period')

############ Tipos de datos complejos
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

##### Ejercicio

planet2={
    'name': 'Mars',
    'moons': 2
}

print(f'{planet2["name"]} has {planet2["moons"]} moon(s)')

planet2['circumference (km)']={
    'polar':6752,
    'equatorial': 6792
}
print(f'{planet2["name"]} has a polar circumference of {planet2["circumference (km)"]["polar"]}')

########################}
######## Diccionarios Dinamicos

# Recuperacion de claves Keys()
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}:{rainfall[key]} cm')

##Determinacion de la exixtencia de una clave en un diccionario  in

if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

## Recuperacion de todos los valores values()

total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'there was {total_rainfall} cm in  the last quarter')
print(' ')
########################
###### EJERCICIO #######

planet_moons = {
    'mercury': 0,
    'venus' : 0,
    'earth' : 1,
    'mars' : 2,
    'jupiter' : 79,
    'saturn' : 82,
    'uranus' : 27,
    'neptune' : 14,
    'pluto' : 5,
    'haumea' : 2,
    'makemake': 1,
    'eris':1
}

moons= planet_moons.values()
print(moons)
total_planets = len(planet_moons.keys()) #len devuelve el tamaño del diccionario
print(planet_moons.keys())


total_moons= 0
for moon in moons:
    total_moons = total_moons + moon

print(total_moons)

average =total_moons/ total_planets
print(f'Each planet has an average of {average} moons')