def binary_search(arr, target):
    """
    Realiza una búsqueda binaria en una lista ordenada.

    Args:
        arr (list): La lista ordenada en la que buscar.
        target (int): El valor objetivo a encontrar.

    Returns:
        int: El índice del valor objetivo en la lista, o -1 si no se encuentra.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Ejemplo de uso
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15]
valor_objetivo = 9
resultado = binary_search(lista_ordenada, valor_objetivo)

if resultado != -1:
    print(f"El valor objetivo {valor_objetivo} se encuentra en el índice {resultado}.")
else:
    print(f"El valor objetivo {valor_objetivo} no se encuentra en la lista.")
