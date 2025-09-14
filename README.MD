# TASK DA-1-28
Программа выполняет **one-hot кодирование** категориальных данных без использования `pandas.get_dummies`.  

# установка зависимостей:
```
pip install -r requirements.txt
```

---

# функция для one-hot кодирования категориальных значений  

```python
one_hot, unique = one_hot_encode(categories)
```

- `categories` – список или массив категориальных значений (например, `['red', 'blue', 'green']`).  
- `unique` – массив уникальных категорий, сохранённых в порядке первого появления.  
- `one_hot` – матрица (размер `N x K`), где `N` – количество элементов, `K` – количество уникальных категорий.  

---

# пример использования  

```python
categories = ['red', 'red', 'blue', 'red', 'green']
one_hot, unique = one_hot_encode(categories)

print(f"Уникальные категории: {unique}")
print("One-hot кодировка:")
print(one_hot)
```

Вывод:  

```
Уникальные категории: ['red' 'blue' 'green']
One-hot кодировка:
[[1 0 0]
 [1 0 0]
 [0 1 0]
 [1 0 0]
 [0 0 1]]
```

---

#обработка ошибок  

- Если входные данные пустые → `ValueError("The input data is empty...")`  
- Если передан неподдерживаемый тип данных → `TypeError("A list or numpy array is expected.")`  
