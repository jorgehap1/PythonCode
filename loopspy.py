#bucle While
# Create the variable for user input
user_input = ''
# Create the list to store the values
inputs = []

# The while loop
while user_input.lower() != 'done':
    # Check if there's a value in user_input
    if user_input:
        # Store the value in the list
        inputs.append(user_input)
    # Prompt for a new value
    user_input = input('Enter a new value, or done when done')
###############
#### EJERCICIO
new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet, or done if done')

print(planets)


##### Bucles for
countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀")

""" El bucle for es una instrucción con cinco partes importantes:

La palabra for, seguida de un espacio.
El nombre de la variable que quiere crear para cada valor de la secuencia (number).
La palabra in, entre espacios.
El nombre de la lista (countdown, en el ejemplo anterior) u objeto iterable que quiere recorrer en bucle, seguido de dos puntos (:).
El código que quiere ejecutar para cada elemento del objeto iterable, separado por espacios en blanco anidados.
Vamos a cambiar ese código para que espere un segundo entre cada número mediante la función sleep(): """

for planet in planets:
    print(planet)