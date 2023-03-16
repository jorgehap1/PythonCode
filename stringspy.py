""" En Python, las cadenas son inmutables. Es decir, no pueden cambiar.
Esta propiedad del tipo de cadena puede ser sorprendente, 
ya que Python no proporciona errores al modificar cadenas. """

fact = "the moon has no atmosphere."
two_facts = fact + "No sound can be heard on the Moon."
two_facts
'The Moon has no atmosphere.No sound can be heard on the Moon.'

##Las operaciones en las cadenas siempre generan cadenas nuevas como resultado.


## Texto Multilinea
""" Usar un carácter de nueva línea (\n).
Usar comillas triples """

multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)
 
multiline2 = """Facts about the Moon:
 There is no atmosphere.
 There is no sound."""
print(multiline2)
print(' ')

##.title()
t=fact.title()
print(t)

##División de una cadena

temperatures = """Daylight: 260 F
... Nighttime: -280 F"""
print(temperatures .split())

print(' ')
## La manera más sencilla de detectar si existe una palabra,
#  un carácter o un grupo de caracteres determinados en una cadena es usar el operador ""in"""
"Moon" in "This text will describe facts and challenges with space travel"
##False
"Moon" in "This text will describe facts about the Moon"
##True

## .find()

""" El método .find() devuelve -1 cuando no se encuentra la palabra, 
o bien devuelve el índice (el número que representa la posición en la cadena). 
Así es como se comportaría si busca la palabra Mars: """

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""
temperatures.find("Moon")

temperatures.find("Mars")

## .count() cuenta el numero total de repeticiones de una palabra

##
## python distinguen mayúsculas de minúsculas, 
# lo que significa que Luna y luna se consideran palabras diferentes
"The Moon And The Earth".lower() ##minusculas
"The Moon And The Earth".upper() #mayusculas
print(' ')

## para eXtraer informacion

Extraer = "Mars Average Temperature: -60 C"

parts = Extraer.split(':')

##['Mars average temperature', ' -60 C']
print(parts[-1]) #El uso de [-1] en la lista devuelve el último elemento que, en este ejemplo, es la temperatura.
##' -60 C'

#En el caso de los números negativos,
#  el guion se agrega como prefijo al número
#  y se puede detectar con el método .startswith():

"-60".startswith('-')

# .replace()

## .join() para unir caracteres volver a agruparlos 
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
'\n'.join(moon_facts)

print(' ')

#### EJERCICIO #####

text= """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
print(text)


#Separate the paragraph into sentences
sentences=text.split('. ') ## el espacio es para no tomer el punto del final
print(sentences)


##Find keywords
for sentence in sentences:
    if 'temperature' in sentence: ## devuelve verdadero
        print(sentence)



####### Formato de signo de porcentaje (%) ES poco usado
"""El marcador de posición de la variable de la cadena es %s"""

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage)

print("""Both sides of the %s get the same amount of sunlight,
     but only one side is seen from %s because
    the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

####
######### El método format()

mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))

print("""You are lighter on the {0}, because on the {0} 
    you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))

print("""You are lighter on the {moon}, because on the {moon} 
     you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))

####Acerca de las cadenas f-strings
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")
print(' ')

####### Ejercicio#####

name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'

template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""


print(template.format(name=name, planet=planet, gravity=gravity))
