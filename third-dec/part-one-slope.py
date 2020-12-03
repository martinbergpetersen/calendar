def find_trees(roads):
    x = 0
    trees = 0
    tree = "#"
    for road in roads:
        idx = x % len(road)
        if tree == road[idx]:
            trees += 1
        x += 3

    return trees


if __name__ == "__main__":
    with open("reports.txt") as f:
        grid = f.read().splitlines()
    result = find_trees(grid)

    print(result)
