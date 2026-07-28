def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if arr1 == arr2:
        return True
    for it in range(len(arr1)):
        if (arr2[it:] + arr2[:it] == arr1):
            return True
    return False

def array_rotation_better(arr1: list, arr2: list) -> bool:
    n = len(arr1)
    doubled = arr1 + arr1
    return n == 0 or any(doubled[i:i+n] == arr2 for i in range(n))

print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
print(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))
print(array_rotation_detector([1, 2, 3], [3, 2, 1]))
print(array_rotation_detector([1, 2], [1, 2, 3]))
print(array_rotation_detector([], []))

print("------------------")
print(array_rotation_better([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
print(array_rotation_better([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))
print(array_rotation_better([1, 2, 3], [3, 2, 1]))
print(array_rotation_better([1, 2], [1, 2, 3]))
print(array_rotation_better([], []))

