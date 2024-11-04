def remove_element(arr, *args):
    return [i for i in arr if not i in args]

def unique(arr):
    res = []
    [res.append(i) for i in arr if not i in res]
    return res

def difference(arr_1, arr_2):
    return [i for i in arr_1 if not i in arr_2]


x = [1, 2, 3, 4, 5]
y = [2, 1, 1, 3, 2]


print(remove_element(x, 1, 0, 5, -2))
print(unique(y))
print(difference(x, y))