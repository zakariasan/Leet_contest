
def arr_rot(arr1: list, arr2: list) -> bool:
    pwn = []
    if len(arr1) == len(arr2):
        if arr1 == arr2:
            return True
        for item in range(len(arr1)):
            pwn = arr1[item:] + arr1[:item]
            if pwn == arr2:
                return True
    return False


print(arr_rot([1,2,4], [4,1,2]))
print(arr_rot([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]) )
print(arr_rot([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))
print(arr_rot([1, 2, 3], [3, 2, 1]) )
print(arr_rot( [1, 2], [1, 2, 3] ) )
print(arr_rot( [], [] ) )

