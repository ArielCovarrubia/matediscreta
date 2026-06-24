# Define la función principal que recibe la lista a ordenar como argumento
def shell_sort(lista):
    # Obtiene la cantidad total de elementos dentro de la lista y la guarda en 'largo'
    largo = len(lista)
    
    # Si la lista no tiene elementos o solo tiene uno, ya está ordenada, así que la devuelve de inmediato
    if largo <= 1:
        return lista
        
    # Calcula el primer "salto" (gap) dividiendo el largo de la lista por 2 usando división entera
    salto = largo // 2
    
    # Comienza un ciclo que se ejecutará mientras el tamaño del salto sea mayor a 0
    while salto > 0:
        # Recorre la lista desde la posición del 'salto' actual hasta el final del arreglo
        for i in range(salto, largo):
            # Guarda temporalmente el valor actual que vamos a comparar y reubicar
            valor_temporal = lista[i]
            # Registra la posición actual del elemento que estamos evaluando
            posicion = i
            
            # Ciclo que compara el valor actual con los elementos que están a una distancia de "salto" hacia atrás
            # Se detiene si llegamos al inicio del salto o si el elemento anterior ya es menor o igual
            while posicion >= salto and lista[posicion - salto] > valor_temporal:
                # Copia el elemento más grande (el que está atrás) hacia la posición de adelante
                lista[posicion] = lista[posicion - salto]
                # Mueve el índice hacia atrás (la distancia del salto) para seguir verificando
                posicion -= salto
                
            # Coloca el valor que teníamos guardado temporalmente en su posición correcta final
            lista[posicion] = valor_temporal
            
        # Reduce el tamaño del salto a la mitad para la siguiente fase del algoritmo (división entera)
        salto //= 2
        
    # Devuelve la lista completamente ordenada una vez que el salto llega a 0
    return lista

# Muestra un mensaje en consola pidiendo al usuario que ingrese los números separados por espacios
entrada_usuario = input("Ingrese una lista de números (pueden ser enteros o decimales con punto) separados por espacios: ")

# Toma el texto del usuario, lo divide por cada espacio, convierte cada fragmento a flotante (decimal) y lo transforma en una lista
mi_lista = list(map(float, entrada_usuario.split()))

# Imprime en pantalla la lista original tal como la ingresó el usuario
print("\nArreglo original:", mi_lista)

# Ejecuta la función shell_sort pasando la lista creada y almacena el resultado final
lista_ordenada = shell_sort(mi_lista)

# Imprime en la consola el resultado final con la lista ya ordenada de menor a mayor
print("Arreglo ordenado:", lista_ordenada)