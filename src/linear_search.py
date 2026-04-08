from src.my_array import MyArray


def linear_search(array: MyArray, target: int) -> int:
    """
    Realiza uma busca em um MyArray.

    Deve retornar o índice da primeira ocorrência do valor,
    ou -1 caso o valor não esteja presente.
    """
    for i in range(array.size()):
        if array.get(i) == target:
            return i
    return -1

