from src.my_array import MyArray


def binary_search(array: MyArray, target: int) -> int:
    """
    Realiza busca binária em um array ordenado.

    Deve retornar o índice do elemento ou -1 caso não encontrado.
    """
    low = 0
    high = len(array) - 1

    while low <= high:

        mid = (low + high) // 2
        guess = array[mid]

        if guess == target:
            return mid
        
        if guess > target:
            high = mid - 1

        else:
            low = mid + 1

    return -1
