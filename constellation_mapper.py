def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    out = []
    res1 = []
    for _ in range(size):
        res1.append('.')
    for item in range(size):
        res = res1.copy()
        for line in range(size):
            if (item, line) in stars:
                res[line] = '*'
        res = ''.join(res)
        out.append(res)
    return out


print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
print(constellation_mapper([(0, 0), (0, 1), (0, 2), (1, 1), (2, 2)], 3))
print(constellation_mapper([(0, 0), (5, 5), (2, 2)], 3))
print(constellation_mapper([(0, 0), (5, 5)], 2))
