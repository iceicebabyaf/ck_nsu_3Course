import numpy as np

categories = np.array(['red', 'red', 'blue', 'red'])
unique = np.array(list(dict.fromkeys(categories.tolist())))
one_hot = (categories[:, None] == unique[None, :]).astype(int)

print(f'unique categories:{unique}')
print(one_hot)
