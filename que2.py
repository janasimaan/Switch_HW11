def brute_common_elements3(arr1, arr2, arr3):
    common_elements = []

    for elem in arr1:
        if elem in arr2 and elem in arr3:
            common_elements.append(elem)

    return common_elements


def common_elements3(arr1, arr2, arr3):
    set1 = set(arr1)
    set2 = set(arr2)
    set3 = set(arr3)

    common_elems = set1.intersection(set2).intersection(set3)
    return list(common_elems)

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8]
arr3 = [0, 4, 5, 6, 7, 2]

print(common_elements3(arr1, arr2, arr3))
print(brute_common_elements3(arr1, arr2, arr3))