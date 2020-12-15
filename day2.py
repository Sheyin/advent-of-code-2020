import re

filename = "day2input.txt"
data = []
validPasswordCount = 0

input = open(filename, "r")

for _ in input:
    line = _.rstrip()
    splitLine = re.split(r'[: -]', line)
    splitLine.remove("")

    # Parsing number range
    minQuantity = splitLine[0]
    maxQuantity = splitLine[1]
    letterRequired = splitLine[2]
    password = splitLine[3]

    # At this point the data should be neatly organized
    # minQuantity, maxQuantity - int values for number of letterRequired
    # letterRequired - the letter in question required in password
    # password - the string to check for the specified letter range

    # Assembling regex pattern - I'm not sure if I can do this in one line
    pattern = letterRequired + "{" + minQuantity + "," + maxQuantity + "}"

    # Now to do the checking....
    if re.search(pattern, password):
        validPasswordCount += 1
        print("A valid password: " + str(re.search(pattern, password)) +
              " pattern: " + pattern + " password: " + password)
    # Should return None if not found, so it shouldn't trigger statement.

print("Final results: " + str(validPasswordCount) + " valid passwords.")
