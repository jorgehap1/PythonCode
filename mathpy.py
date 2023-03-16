## SUMA ##
answer = 30+12
print(answer)
print(' ')

## Resta ##
difference = 30 - 12
print(difference)

## Multiplicacion ##
## Division ##
""" redondear hacia abajo, usando lo que se conoce como división de múltiplo inferior. 
Para realizar una división de este tipo en Python, debe utilizar //. """
print(' ')
seconds = 1024
display_minutes = seconds // 60
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)

### Orden de las operaciones ###
""" Paréntesis
Exponentes
Multiplicación y división
Suma y resta """


#### EJERCICIO #####

first_planet = 149597870
second_planet = 778547200

distance_km =second_planet-first_planet
print(distance_km)

distance_mi = distance_km / 1.609344
print(distance_mi)

###Conversión de cadenas en números
demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

## Valor obsoluto abs
print(abs(16 - 39))

## Redondeo
print(round(14.5))

from math import ceil, floor

round_up = ceil(12.5) ## redondear siempre hacia arriba 
print(round_up)

round_down = floor(12.5) ## redondear siempre hacia abajo
print(round_down)
print(' ')
#################################################
##### EJERCICIO ############# 
#################################

first_planet_input = input('Enter the distance from the sun for the first planet in KM ')
second_planet_input = input('Enter the distance from the sun for the second planet in KM ')

first_planet = int(first_planet) 
second_planet = int(second_planet)

distance_km = second_planet-first_planet
print(abs(distance_km))
