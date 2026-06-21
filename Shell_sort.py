def shell_sort(arr):
    n = len(arr)
    # Inicializamos la brecha (gap) a la mitad del tamaño del arreglo
    gap = n // 2

    # El ciclo continúa mientras la brecha sea mayor que 0
    while gap > 0:
        # Hacemos un ordenamiento por inserción para este tamaño de brecha
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # Desplazamos los elementos que son mayores que temp hacia adelante
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                
            # Colocamos temp en su posición correcta
            arr[j] = temp
            
        # Reducimos la brecha a la mitad para la siguiente vuelta
        gap //= 2

# Ejemplo de uso:
mi_lista = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
print("Arreglo original:", mi_lista)

shell_sort(mi_lista)
print("Arreglo ordenado:", mi_lista)