### Exception Handling ###

numberOne = 5 
numberTwo = 5
numberTwo = "1"


if type(numberTwo) == int:
  print(numberOne + numberTwo)
else:
  print("No se cumplio if")

# try except

'''
try except es una estructura de control que permite manejar las excepciones que se puedan 
producir en el código, es decir, los errores que se puedan producir en tiempo de ejecución, 

try es el bloque de código que se va a ejecutar y 
except es el bloque de código que se va a ejecutar si se produce una excepción, es decir, si se produce un error en el bloque de 
código try, se ejecuta el bloque de código except, si no se produce ningún error en el bloque 
de código try, se ejecuta el bloque de código else, que es opcional, y se ejecuta si no se 
produce ningún error en el bloque de código try
'''

try:
  print(numberOne + numberTwo)
  print("No se ha producido error")
except:
  print("No se cumplio except")


# try except else

try:
  print(numberOne + numberTwo)
  print("No se ha producido error try")
except:
  # Se ejecuta si se produce un error en el bloque de código try
  print("No se cumplio")
else:
  # Se ejecuta si no se produce ningún error en el bloque de código try
  print("Se ha ejecutado el bloque else")
  print("La ejecución continua")

# try except else finally

try:
  print(numberOne + numberTwo)
  print("No se ha producido error try")
except:
  # Se ejecuta si se produce un error en el bloque de código try
  print("No se cumplio")
else: # Opcional
  # Se ejecuta si no se produce ningún error en el bloque de código try
  print("Se ha ejecutado el bloque else")
  print("La ejecución continua")
finally: # Opcional
    # Se ejecuta siempre, se produzca o no un error en el bloque de código try
    print("Se ha ejecutado el bloque finally")



# Excepciones por tipo

try:
  print(numberOne + numberTwo)
  print("No se ha producido error try")
except TypeError: # Se ejecuta si se produce un error de tipo TypeError en el bloque de código try
  # Se ejecuta si se produce un error en el bloque de código try
  print("No se cumplio except TypeError")
except ValueError: # Se ejecuta si se produce un error de tipo ValueError en el bloque de código try
    # Se ejecuta si se produce un error en el bloque de código try
    print("No se cumplio except ValueError")


# Captura de la información de la excepción
try:
    print(numberOne + numberTwo)
    print("No se ha producido error try")
except ValueError as error:
  print ("No se cumplio except ValueError")
  print(error) # Imprime la información de la excepción
except Exception as error:
  print ("No se cumplio except Exception")
  print(error) # Imprime la información de la excepción