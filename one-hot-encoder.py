import numpy as np
from typing import List, Union

def one_hot_encode(categories: Union[List[str], np.ndarray]) -> np.ndarray:
    """
    Выполняет one-hot кодирование категориальных данных без использования pandas.get_dummies.

    Args:
        categories (list | np.ndarray): Список или массив категориальных значений.

    Returns:
        np.ndarray: One-hot матрица (размер: N x K), где 
                    N - количество элементов, 
                    K - количество уникальных категорий.

    Raises:
        ValueError: Если входные данные пустые или содержат неподдерживаемые типы.
    """
    if categories is None or len(categories) == 0:
        raise ValueError("The input data is empty. Send a list or an array of categories.")

    if not isinstance(categories, (list, np.ndarray)):
        raise TypeError("A list or numpy array is expected.")

    categories = np.array(categories, dtype=str)
    unique = np.array(list(dict.fromkeys(categories.tolist())))

    one_hot = (categories[:, None] == unique[None, :]).astype(int)

    return one_hot, unique

"""
Example:
"""
# if __name__ == "__main__":

#     categories = ['red', 'red', 'blue', 'red', 'green']
#     one_hot, unique = one_hot_encode(categories)

#     print(f"Уникальные категории: {unique}")
#     print("One-hot кодировка:")
#     print(one_hot)