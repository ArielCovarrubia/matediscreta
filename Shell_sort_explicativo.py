# 1. Definimos la función llamada 'shell_sort' que recibe como parámetro 'lista'
def shell_sort(lista):
    # 2. Calculamos cuántos elementos tiene la lista y lo guardamos en 'largo'
    largo = len(lista)
    
    # 3. Si la lista tiene 0 o 1 elemento, ya está ordenada, así que la devuelve de inmediato
    if largo <= 1:
        return lista
        
    # 4. Calculamos el 'salto' inicial (la brecha o gap) usando división entera (// 2)
    # Por ejemplo, si la lista tiene 6 elementos, el primer salto será de 3
    salto = largo // 2
    
    # 5. El bucle principal continuará mientras el salto sea mayor que cero (sea 1 o más)
    while salto > 0:
        
        # 6. Recorremos la lista desde la posición del 'salto' hasta el final ('largo')
        # Esto nos permite comparar elementos separados por la distancia del 'salto'
        for i in range(salto, largo):
            
            # 7. Guardamos el valor actual en una variable temporal para no perderlo al mover otros números
            valor_temporal = lista[i]
            
            # 8. Registramos la posición actual del elemento que estamos evaluando
            posicion = i
            
            # 9. Bucle de ordenamiento por inserción: compara el elemento actual con el que está un 'salto' hacia atrás.
            # Se repite si no nos salimos del inicio de la lista (posicion >= salto) 
            # y si el elemento de atrás es mayor que nuestro 'valor_temporal'
            while posicion >= salto and lista[posicion - salto] > valor_temporal:
                
                # 10. Como el de atrás es mayor, movemos ese elemento hacia adelante ocupando el lugar actual
                lista[posicion] = lista[posicion - salto]
                
                # 11. Retrocedemos la posición según el 'salto' para verificar si el elemento de más atrás también es mayor
                posicion -= salto
                
            # 12. Cuando encontramos el lugar correcto (donde el de atrás ya no es mayor), colocamos el 'valor_temporal' ahí
            lista[posicion] = valor_temporal
            
        # 13. Reducimos el salto a la mitad para la siguiente ronda de comparaciones más cercanas
        salto //= 2
        
    # 14. OPCEÓN CORREGIDA: Recorremos la lista ya ordenada con una lista de comprensión.
    # Si un número termina en .0 (es entero flotante), lo convierte a 'int' puro; si tiene decimales reales, lo deja como 'float'.
    lista_limpia = [int(x) if x.is_integer() else x for x in lista]
    
    # 15. Devolvemos la nueva lista limpia y sin ceros estéticos al final
    return lista_limpia

# 16. Pedimos al usuario que ingrese los números separados por un espacio en blanco
entrada_usuario = input("Ingrese una lista de números (pueden ser enteros o decimales con punto) separados por espacios: ")

# 17. Tomamos el texto ingresado, lo separamos por espacios (.split()) y convertimos cada dato a float usando map()
mi_lista = list(map(float, entrada_usuario.split()))

# 18. Imprimimos en pantalla la lista original tal como la ingresó el usuario (convertida a float)
print("\nArreglo original:", mi_lista)

# 19. Llamamos a nuestra función pasando 'mi_lista' y guardamos el resultado limpio en 'lista_ordenada'
lista_ordenada = shell_sort(mi_lista)

# 20. Imprimimos el resultado final ordenado y formateado estéticamente
print("Arreglo ordenado:", lista_ordenada)