filename = "day1input.txt"
data = []

input = open(filename, "r")

for line in input:
    data.append(int(line.rstrip()))

# I don't think you can do less than O(n^2) for this one....
print("Part One: ")
for x in range(0, len(data)):
    for y in range(1, len(data)):
        if (data[x] + data[y] == 2020):
            print(
                f"The answer is {data[x]} + {data[y]} = 2020, {data[x]} * {data[y]} = {data[x] * data[y]}")


# Part 2 is even crazier....
print("Part Two: ")
for x in range(0, len(data)):
    for y in range(1, len(data)):
        for z in range(1, len(data)):
            if (data[x] + data[y] + data[z] == 2020):
                print(
                    f"The answer is {data[x]} + {data[y]} + {data[z]} = 2020, {data[x]} * {data[y]} * {data[z]} = {data[x] * data[y] * data[z]}")
