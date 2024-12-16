def common_elements1(arr1, arr2):
    common_elems1 = []
    for i in arr1:
        for j in arr2:
            if i==j and i not in common_elems1:
                common_elems1.append(i)
    return common_elems1

def common_elements2(arr1, arr2):
    set_arr2 = set(arr2)
    common_elems2 = [i for i in arr1 if i in set_arr2]
    return common_elems2


arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
result1 = common_elements1(arr1, arr2)
result2 = common_elements2(arr1, arr2)
print(result1)
print(result2)