def cuadradosLista(arreglo):

    enteros_positivos = list(filter(lambda x: x > 0 and x.is_integer(), arreglo))
    
    cuadrados = list(map(lambda x: x ** 2, enteros_positivos))
    
    return cuadrados

cuadrados_enteros = cuadradosLista([-3, 4.8, 5, 3, -3.2])
print(cuadrados_enteros)