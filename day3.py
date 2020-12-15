
def main():
    # Get file input
    filename = "./data/" + "day3input.txt"
    map = []
    input = open(filename, "r")

    for _ in input:
        line = _.rstrip()
        map.append(line)

    treeCountOne = countTrees(map, 3, 1)
    print("Part one trees found: " + str(treeCountOne))

    # Part two
    slope1 = countTrees(map, 1, 1)
    print(f"Slope 1: {slope1} trees")
    slope2 = treeCountOne
    print(f"Slope 2: {slope2} trees")
    slope3 = countTrees(map, 5, 1)
    print(f"Slope 3: {slope3} trees")
    slope4 = countTrees(map, 7, 1)
    print(f"Slope 4: {slope4} trees")
    slope5 = countTrees(map, 1, 2)
    print(f"Slope 5: {slope5} trees")
    product = slope1 * slope2 * slope3 * slope4 * slope5
    print("Part Two product: " + str(product))
    # I get 5,191,884,940 which is apparently too big
    # (82, 242, 71, 67, 55)


def countTrees(map, right, down):
    # The map repeats to the right
    treeCount = 0
    col = 0
    height = len(map)
    for row in range(0, height):
        if row + down >= len(map):
            break
        line = map[row + down]
        col += right
        if isTree(col, line):
            treeCount += 1
    return treeCount


# Is this spot a tree? Returns T/F
def isTree(index, row):
    if row[positionOf(index, row)] == "#":
        return True
    else:
        return False

# Not the best name, but I suppose it'll read better in code.
# Recalculates the position of the column (index) in the line
# Since the map repeats to the right.


def positionOf(index, row):
    length = len(row)
    if index >= length:
        index = index % length
    return index


if __name__ == "__main__":
    main()
