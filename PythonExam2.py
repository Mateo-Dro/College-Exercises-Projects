#Mateo Díaz DNI: 44762094

#Cargar listas
def cargar():
    palabras = []
    n = int(input("Escriba la cantidad de palabras a ingresar: "))
    for _ in range(n):
        palabra = input("Ingrese cualquier palabra: ")
        palabras.append(palabra)
    return palabras

#Ordenar la lista de palabras (esta vez sin crear otra)
def ordenar_palabras_longitud(palabras):
    for i in range(len(palabras)):
        for j in range(len(palabras) - i - 1):
            if (len(palabras[j]) > len(palabras[j + 1])):
                aux = palabras[j]
                palabras[j] = palabras[j + 1]
                palabras[j + 1] = aux
    return palabras #Esta vez decidí usar la misma lista y modificarla. Si al final era necesario crear otra, se hace casi idéntico a la 4ta función de Diaz_p1. 

#Buscador de letras 
def encontrar_palabras_con_letra(palabras, letra):
    incluye = []
    for _ in palabras:
        if (letra.lower() in _) or (letra.upper() in _) or (letra.capitalize() in _): #Para asegurarme de que independientemente de lo que ingrese el usuario, funcione. Capitalize es para cuando ingresan más de una letra.
            incluye.append(_) 
    return incluye
    
#Main
palabras = cargar() 
print("\nLa lista de palabras ordenada de menor a mayor según su longitud: ")
for _ in ordenar_palabras_longitud(palabras):
    print(_)
letra = input("\nIngrese la letra que quiere buscar: ")
print(f"Estas son las palabras que incluyen esa letra: {', '.join(map(str, encontrar_palabras_con_letra(palabras, letra)))}")