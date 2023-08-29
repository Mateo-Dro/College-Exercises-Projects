#Mateo Díaz DNI: 44762094

#Cargar listas
def cargar():
    empleados = []
    sueldos = []
    n = int(input("Escriba la cantidad de empleados a ingresar: "))
    for _ in range(n): #en Visual Studio Code uso "_" para evitar ciertos avisos en la terminal. Pero funciona perfectamente bien con otro valor.
        nombre = input("Ingrese el nombre del empleado: ")
        nombre = nombre.capitalize() 
        suel = int(input("Ingrese su sueldo: "))
        empleados.append(nombre) 
        sueldos.append(suel)
    return (empleados, sueldos)

#Calcular promedios
def calcular_promedio_sueldos(sueldos):
    promedio = 0
    for _ in range(len(sueldos)):
        promedio += sueldos[_] #podría usar la función sum, pero para mantenerse acorde a lo que vimos en clase lo hago de este modo. 
    promedio /= len(sueldos) #devuelvo el promedio en valores reales. Podría haber usado "//" para valores enteros.
    return promedio

#Obtener el sueldo máximo del empleado
def obtener_empleado_sueldo_max(empleados, sueldos):
    smax = 0 #smax es igual a la posición 0 de la lista.
    for i in range(1, len(sueldos)): #podría también usar la función max. 
        if (sueldos[i] > sueldos[smax]):
            smax = i
    return empleados[smax]
 
#Ordenamiento de lista de menor a mayor en base al sueldo  
def ordenar_por_sueldo(empleados, sueldos):
    empleados2 = empleados[:] #Personalmente entendí que se tenían que hacer nuevas listas. En caso contrario, se aplica la misma técnica que apliqué pero en las originales.
    sueldos2 = sueldos[:] #Una alternativa a toda esta función se encuentra debajo del main. 
    for i in range(len(sueldos2)):
        for j in range(len(sueldos2)-i-1):
            if (sueldos2[j] > sueldos2[j+1]):
                aux=sueldos2[j]
                sueldos2[j] = sueldos2[j+1]
                sueldos2[j + 1] = aux
                aux=empleados2[j]
                empleados2[j] = empleados2[j + 1]
                empleados2[j + 1] = aux
    return (empleados2, sueldos2) #Devuelvo valores en lugar de imprimirlos, como dice la consigna.

#Main
empleados, sueldos = cargar()
emp_ordenados, suel_ordenados = ordenar_por_sueldo(empleados, sueldos)
print("\nLista ordenada por sueldo: ")
for i, j in zip(emp_ordenados, suel_ordenados): 
    print(f"{i} | ${j}") 
    #Esto podría haberlo hecho dentro de la última función. Pero la consigna pedía devolver dos listas distintas, así que usé este método (un poco más obtuso) para imprimir de manera ordenada y linda los valores.
print(f"\nEl promedio de sueldo es: ${calcular_promedio_sueldos(sueldos)}")
print(f"El empleado con mayor sueldo es: {obtener_empleado_sueldo_max(empleados, sueldos)}")
#El código podría haber sido más limpio pero decidí dejar muchos comentarios para explicar estas cosas, pues estoy experimentando con muchas cosas que aprendí estas semanas.



#Otra alternativa para la cuarta función:

#def ordenar_por_sueldo(empleados, sueldos):
#    empleados_sueldos = list(zip(empleados, sueldos))
#    empleados_sueldos.sort(key=lambda x: x[1])
#    print(f"La lista ordenada es: {'-'.join(map(str, empleados_sueldos))}")      
##str sirve para devolver como cadena los valores de la lista, map sirve para que se aplique la función str en todos los valores de la lista, y join sirve para concatenarlos. 
##La función zip sirve para juntar dos listas en una sola. Sort para ordenar dicha combinación y key=lambda es para ordenarlo en función del segundo elemento de las tuplas de la lista. 
