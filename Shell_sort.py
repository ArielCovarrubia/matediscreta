def shell_sort(lista):
    largo = len(lista)
    
    if largo <= 1:
        return lista
        
    salto = largo // 2
    
    while salto > 0:
        for i in range(salto, largo):
            valor_temporal = lista[i]
            posicion = i
            
            while posicion >= salto and lista[posicion - salto] > valor_temporal:
                lista[posicion] = lista[posicion - salto]
                posicion -= salto
                
            lista[posicion] = valor_temporal
            
        salto //= 2
        
    return lista

entrada_usuario = input("Ingrese una lista de números (pueden ser enteros o decimales con punto) separados por espacios: ")
mi_lista = list(map(float, entrada_usuario.split()))

print("\nArreglo original:", mi_lista)
lista_ordenada = shell_sort(mi_lista)
print("Arreglo ordenado:", lista_ordenada)