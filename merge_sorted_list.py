def merge_sorted_list(lists: list[list[int]]) -> list[int]:
    comb = []
    for item in lists:
        comb += item
    if len(comb) > 1:
        mi = min(comb)
        ma = max(comb)

        for i in range(mi, ma):
            if i not in comb:
                comb.append(i)
    return sorted(comb)


print(merge_sorted_list([[1, 4, 5], [1, 3, 4], [2, 6]]))
print(merge_sorted_list([[1, 2, 3], [], [0, 4]]))
print(merge_sorted_list([]))
print(merge_sorted_list([[], []]))
