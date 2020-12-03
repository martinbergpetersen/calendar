from collections import namedtuple
from functools import reduce

Coordinate = namedtuple("Coordinate", ["x", "y"])


def find_trees(roads, coordinate):
    _x = 0
    trees = 0
    tree = "#"
    slices = slice(0, None, coordinate.y)
    for road in roads[slices]:
        idx = _x % len(road)
        if tree == road[idx]:
            trees += 1
        _x += coordinate.x

    return trees


if __name__ == "__main__":
    with open("reports.txt") as f:
        data = f.read().splitlines()
    coordinates = [
        Coordinate(1, 1),
        Coordinate(3, 1),
        Coordinate(5, 1),
        Coordinate(7, 1),
        Coordinate(1, 2),
    ]
    result = reduce(
        lambda a, b: a * b, [find_trees(data, coordinate) for coordinate in coordinates]
    )

    print(result)
