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
        
    if len(lista) > 0 and isinstance(lista[0], (int, float)):
        lista_limpia = [int(x) if hasattr(x, 'is_integer') and x.is_integer() else x for x in lista]
        return lista_limpia
        
    return lista

entrada_usuario = input("Ingrese una lista (pueden ser números enteros, decimales o palabras) separados por espacios: ")
elementos = entrada_usuario.split()

mi_lista = []

if elementos:
    try:
        mi_lista = [float(x) for x in elementos]
    except ValueError:
        mi_lista = elementos
else:
    mi_lista = []

print("\nArreglo original:", mi_lista)
lista_ordenada = shell_sort(mi_lista)
print("Arreglo ordenado:", lista_ordenada)