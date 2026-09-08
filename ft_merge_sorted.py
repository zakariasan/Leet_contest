def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    out = []
    res = []
    for item in lists:
        res += item

    if res == []:
        return []
    mini = min(res)
    maxi = max(res)

    for nbr in range(mini, maxi + 1):
        cnt = sum(map(lambda x: 1 if x == nbr else 0, res))
        if nbr in res:
            for el in range(cnt):
                out.append(nbr)

    return out


print(merge_sorted_lists([[1, 3, 5], [2, 4, 6]]))
print(merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]]))
print(merge_sorted_lists([[5], [1, 3], [2, 4]]))

print(merge_sorted_lists([[1, 1, 2], [2, 3, 3]]))
print(merge_sorted_lists([[], [1, 2, 3]]))
print(merge_sorted_lists([[]]))
print(merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]]))
print(merge_sorted_lists([[10], [10], [10]]))
