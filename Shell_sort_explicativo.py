# 1. Se define la función 'shell_sort' que toma como parámetro la lista a ordenar
def shell_sort(lista):
    # 2. Se calcula la cantidad de elementos en la lista y se almacena en 'largo'
    largo = len(lista)
    
    # 3. Si la lista está vacía o tiene un solo elemento, ya está ordenada y se regresa de inmediato
    if largo <= 1:
        return lista
        
    # 4. Se calcula el tamaño del salto inicial dividiendo el largo de la lista entre 2
    salto = largo // 2
    
    # 5. Este bucle se ejecutará mientras el salto sea mayor que 0
    while salto > 0:
        # 6. Se recorre la lista partiendo desde la posición del salto hasta el final
        for i in range(salto, largo):
            # 7. Se guarda el valor actual en una variable temporal para no perderlo al reubicar datos
            valor_temporal = lista[i]
            # 8. Se registra la posición actual del índice evaluado
            posicion = i
            
            # 9. Se comparan los elementos que están separados a la distancia del 'salto'
            # El bucle sigue si la posición es válida y el elemento de atrás es mayor que el actual
            while posicion >= salto and lista[posicion - salto] > valor_temporal:
                # 10. Se desplaza el elemento mayor hacia la derecha
                lista[posicion] = lista[posicion - salto]
                # 11. Se resta el salto a la posición para verificar elementos más atrás en la misma brecha
                posicion -= salto
                
            # 12. Se coloca el valor guardado temporalmente en su posición correcta de esta ronda
            lista[posicion] = valor_temporal
            
        # 13. Se reduce el tamaño del salto a la mitad para la siguiente fase de comparación
        salto //= 2
        
    # 14. Se comprueba si la lista contiene elementos y si el primero es numérico (int o float)
    if len(lista) > 0 and isinstance(lista[0], (int, float)):
        # 15. Si es numérica, transforma a entero (int) solo los números flotantes que terminen en .0
        lista_limpia = [int(x) if hasattr(x, 'is_integer') and x.is_integer() else x for x in lista]
        # 16. Se devuelve la lista numérica limpia sin los decimales .0 innecesarios
        return lista_limpia
        
    # 17. Si la lista es de palabras (str) o viene vacía, se devuelve tal cual como quedó
    return lista

# 18. Se solicita al usuario que ingrese los datos por consola separados por espacios
entrada_usuario = input("Ingrese una lista (pueden ser números enteros, decimales o palabras) separados por espacios: ")
# 19. Se divide el texto ingresado por cada espacio en blanco para generar una lista de elementos individuales
elementos = entrada_usuario.split()

# 20. Se inicializa una variable vacía para almacenar la lista procesada antes de ordenar
mi_lista = []

# 21. Se verifica si el usuario escribió algo en lugar de dejar la entrada vacía
if elementos:
    # 22. Se abre un bloque de prueba para intentar convertir los datos a números
    try:
        # 23. Si todos los elementos se pueden transformar a float, se genera la lista numérica
        mi_lista = [float(x) for x in elementos]
    # 24. Si ocurre un error de valor (porque el usuario ingresó palabras o letras)
    except ValueError:
        # 25. Se asigna la lista original de textos sin hacer conversiones numéricas
        mi_lista = elementos
# 26. En caso de que el usuario no haya escrito nada y presionara Enter directo
else:
    # 27. Se establece la variable como una lista completamente vacía
    mi_lista = []

# 28. Se imprime en pantalla el estado original de la lista ingresada por el usuario
print("\nArreglo original:", mi_lista)
# 29. Se invoca a la función 'shell_sort' pasando 'mi_lista' y se guarda el resultado en 'lista_ordenada'
lista_ordenada = shell_sort(mi_lista)
# 30. Se muestra en la consola el arreglo final perfectamente ordenado y formateado
print("Arreglo ordenado:", lista_ordenada)