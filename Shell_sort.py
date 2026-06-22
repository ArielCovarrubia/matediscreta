def shell_sort(lista):
    """
    Ordena una lista utilizando el método Shell Sort.
    Optimizado y robusto ante listas vacías o de un solo elemento.
    """
    largo = len(lista)
    
    # Validación obligatoria para listas vacías o de 1 elemento (Sección G de la pauta)
    if largo <= 1:
        return lista
        
    # Inicializamos el salto (gap) a la mitad del tamaño del arreglo
    salto = largo // 2
    
    # El ciclo continúa mientras el salto sea mayor que 0
    while salto > 0:
        # Hacemos un ordenamiento por inserción para este tamaño de salto
        for i in range(salto, largo):
            valor_temporal = lista[i]
            posicion = i
            
            # Desplazamos los elementos hacia adelante si son mayores que valor_temporal
            while posicion >= salto and lista[posicion - salto] > valor_temporal:
                lista[posicion] = lista[posicion - salto]
                posicion -= salto
                
            # Colocamos el valor temporal en su posición correcta
            lista[posicion] = valor_temporal
            
        # Reducimos el salto a la mitad para la siguiente iteración
        salto //= 2
        
    return lista

# ==========================================
# BLOQUE DE EJECUCIÓN (Entrada por consola)
# ==========================================
# Solicitamos los datos al usuario en una sola línea separados por espacios
entrada_usuario = input("Ingrese una lista de números separados por espacios: ")

# Convertimos la entrada de texto en una lista de números enteros
mi_lista = list(map(int, entrada_usuario.split()))

print("\nArreglo original:", mi_lista)

# Llamamos a la función y guardamos el resultado ordenado
lista_ordenada = shell_sort(mi_lista)

print("Arreglo ordenado:", lista_ordenada) 