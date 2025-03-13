#Exercise 1
cadena = "Hola, mi nombre es Katherine"
numero = 27
lista = ["manzana", "mangos", "peras"]
booleano = True

print("Presentacion:", cadena)
print("Edad:", numero)
print("Compras:", lista)
print("Sexo_Femenino:", booleano)
print() 

#Exercise 2
cadena = "Hola, mi nombre es Katherine"
letras= cadena[0:3]
print(letras)
print() 

#Exercise 3
lista = ["manzana", "mangos", "peras"]
primera_fruta= lista[0]
print(primera_fruta)
print() 

#Exercise 4
numero = 27
nuevo_numero = numero + 10
print(nuevo_numero)
print() 

#Exercise 5
lista = ["manzana", "mangos", "peras"]
ultima_fruta = lista[-1]
print(ultima_fruta)
print() 

#Exercise 6
names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')
print(names_list)
print() 

#Exercise 7
cadena = "Hola, mi nombre es Katherine"
primera_palabra = cadena.split()[0]
mayuscula = primera_palabra.upper()
resto_cadenas = cadena [len(primera_palabra):]
nueva_cadena = mayuscula + resto_cadenas
print(nueva_cadena)
print() 

#Exercise 8
numero = 27
frase = f"Mi edad es {numero}"
print(frase)
print() 

#Exercise 9
print('Hello world')
print()

#Exercise 10
saludo = 'Hola, un placer conocerte'
print(saludo)

if "Hola" in saludo:
  print("Buscar: Hola")

saludo = saludo.replace('Hola', 'Adios')
print(saludo)
