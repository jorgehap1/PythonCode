## Funciones sin argumentos, se crea funcion con def
def rocket_parts():
    print('payload, propellant, structure')

output= rocket_parts()
output 

## Argumentos opcionales y requeridos

any([True, False, False]) # any() Esta función toma un objeto iterable y devuelve true si algun elemento es true, si esta vacio sale error

str(15) 

##### Exigencia de un argumento
def distance_from_earth(destination):
    if destination == 'Moon':
        return "238,855"
    else:
        return "Unable to compute to that destination"

print(distance_from_earth("d"))

##### varios argumentos 

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print (days_to_complete(238855,75))

### Funciones como argumentos
total_days = days_to_complete(238855,75)
print (round(total_days))


#########################
########## EJERCICIO#####

def generate_report (main_tank,external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank:{main_tank}
    External tank:{external_tank}
    Hydrogen tank:{hydrogen_tank}
     """
    print(output)

generate_report(80,70,75)

### Argumentos de palabra clave  ya definen valores predeterminados 
from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival= now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print(arrival_time(0))

## Combinacion de argumentos y argumentos de palabra clave // se debe definir primero los argumentos y luego las palabras claves

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival= now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

print(arrival_time("Moon", hours=0.13))


#### Argumentos de Variable
def variable_length(*args): #arg es una variable que contiene todos los arguementos 
    print(args)

def sequence_time(*args):
    total_minutes =sum(args)
    if total_minutes < 60:
        return f"total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"

print (sequence_time(4,14,18))

#### Argumentos de palabra clave variable
def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday",pilots=3)

print(" ")

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission: ")
    for title, name in kwargs.items():
        print(f"{title}:{name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")

###############################
##### EJERCICIO #########

def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name} : {value}')

fuel_report(main=50,external=100,emergency=60)






