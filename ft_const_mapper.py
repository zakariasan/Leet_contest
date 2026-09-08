def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    arr = []
    for x in range(dim):
        zaz = ''
        for y in range(dim):
            if (x, y) in stars:
                zaz += '*'
            else:
                zaz += '.'
        arr.append(zaz)
    return arr


print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))
print(constellation_mapper([], 2))
print(constellation_mapper([(0, 0), (0, 0), (1, 1)], 2))
print(constellation_mapper([(0, 0), (5, 5)], 3))

print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))

