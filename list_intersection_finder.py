def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if len(lists) == 0:
        return []
    checks = lists[1:]
    items = lists[0]
    prim = []
    for item in items:
        is_here = 0
        for che in checks:
            if item in che:
                is_here += 1
        if is_here == len(checks) and item not in prim:
            prim.append(item)
    return sorted(prim)


print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))
print(list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]))
print(list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]))
print(list_intersection_finder([[1, 2, 3], [4, 5, 6]]))
print(list_intersection_finder([]))
print(list_intersection_finder([[1, 2, 3], []]))
print(list_intersection_finder([[5]]))
print(list_intersection_finder([[3, 1, 1, 2]]))
