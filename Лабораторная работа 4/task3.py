def delete(list_, index=None):
    list2 = []
    if index is None:
        list2 = list_[:-1]
    else:
        list2 = list_[:index] + list_[index+1:]
    return list2

     # TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]

