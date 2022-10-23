# Tercero Función lambda que recibe nombre, edad y ocupación de una persona y devuelva un diccionario con esta información

nombre =input("digite su nombre: ")
edad = input("digite su edad: ")
ocupacion = input("digite ocupacion: ")

datosPersonales = lambda nombre, edad, ocupacion :{nombre, edad, ocupacion}
print (datosPersonales(nombre, edad, ocupacion))