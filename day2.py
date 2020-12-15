import re

filename = "day2input.txt"
data = []
validPasswordCount = 0
# Troubleshooting only
goodPassword = []
badPassword = []
badPasswordCount = 0

input = open(filename, "r")

for _ in input:
    line = _.rstrip()
    splitLine = re.split(r'[: -]', line)
    splitLine.remove("")

    # Parsing number range
    minQuantity = int(splitLine[0])
    maxQuantity = int(splitLine[1])
    letterRequired = splitLine[2]
    password = splitLine[3]

    # At this point the data should be neatly organized
    # minQuantity, maxQuantity - int values for number of letterRequired
    # letterRequired - the letter in question required in password
    # password - the string to check for the specified letter range

    # Assembling regex pattern - I'm not sure if I can do this in one line
    # pattern = letterRequired + "{" + str(minQuantity) + "," + str(maxQuantity) + "}"
    # This pattern just forms something like q{2,5} which will confirm
    # "qqfd" but will fail "qasq" (not sequential), so a two-step process
    # might be the easiest way to do with (or, use pure Python and not regex)

    # Python only version
    letterCount = 0
    for char in password:
        if char == letterRequired:
            letterCount += 1

    if letterCount >= minQuantity and letterCount <= maxQuantity:
        validPasswordCount += 1

print("Final results: " + str(validPasswordCount) + " valid passwords.")

'''
    # Now to do the checking....
    if re.search(pattern, password):
        validPasswordCount += 1
        goodPassword.append(
            (str(re.search(pattern, password)), pattern, password))
        # print("A valid password: " + str(re.search(pattern, password)) +
        #      " pattern: " + pattern + " password: " + password)
    # Should return None if not found, so it shouldn't trigger statement.
    else:
        badPassword.append(
            (str(re.search(pattern, password)), pattern, password))
        badPasswordCount += 1
'''

'''
print("Bad passwords:")
for x in badPassword:
    #print(x[0] + "\t" + x[1] + "\t" + x[2])
    print(x[1] + "\t" + x[2])
'''
