filename = "day2input.txt"
data = []
validPasswordCount = 0

input = open(filename, "r")

for _ in input:
    line = _.rstrip()
    splitLine = line.split(": ")

    # Parsing number range
    rangeSplit = splitLine[0].split("-")
    minQuantity = int(rangeSplit(0))
    maxQuantity = int(rangeSplit(1))

    letterRequired = splitLine[1]

    password = splitLine[2]

    # At this point the data should be neatly organized
    # minQuantity, maxQuantity - int values for number of letterRequired
    # letterRequired - the letter in question required in password
    # password - the string to check for the specified letter range

    # Now to do the checking....
