def main():
    # Get file input
    filename = "./data/day" + "4" + "input.txt"
    input = open(filename, "r")
    data = []
    raw_data = input.read()
    data = raw_data.split("\n\n")

    partOneRequiredFields = {
        "ecl": True,
        "pid": True,
        "eyr": True,
        "hcl": True,
        "byr": True,
        "iyr": True,
        "cid": False,
        "hgt": True
    }

    validEntries = []
    partOneValidEntries = 0
    for _ in data:
        validPassport = checkFields(_, partOneRequiredFields)
        if validPassport:
            partOneValidEntries += 1
            entryDict = splitData(_)
            # This is for part 2
            if entryDict["valid"]:
                validEntries.append(entryDict)
    print(
        f'Part One: Valid passports: {partOneValidEntries} / Total Entries: {len(data)}')
    # Hopefully still 192 / 259

    # At this point the validEntries array should have a bunch of dictionaries
    # with almost all fields that need to be validated (part 2)
    validatedEntryCount = 0
    for entry in validEntries:
        if validateData(entry):
            validatedEntryCount += 1
    print(
        f'Part Two: Valid passports: {validatedEntryCount} / Total Entries: {len(validEntries)}')


# Pretty much only used for Part 1.  Just verifies whether the entry has the required fields.
def checkFields(entry, fieldsDict):
    requiredFields = fieldsDict.keys()
    for field in requiredFields:
        if field not in entry and fieldsDict[field] == True:
            return False
    return True


# Splits a data entry into its field and data components, and returns a dictionary
# If it returns a {valid:False} it is invalid.  I wanted to separate out the validation but if it's missing data...
def splitData(entry):
    entry = entry.replace("\n", " ")
    splitEntry = entry.split(" ")
    entryDict = {"valid": True}
    for _ in splitEntry:
        data = _.split(":")
        # Don't include pid in this case since it will drop the leading zeroes
        if data[0] in ["byr", "iyr", "eyr"]:
            try:
                entryDict[data[0]] = int(data[1])
            except:
                return {"valid": False}
        elif data[0] == "hgt":
            try:
                # This assigns an entry "hgt" with just the number
                entryDict[data[0]] = int(data[1][:-2])
                # This assigns an entry "hgtUnit" with the units only
                entryDict["hgtUnit"] = data[1][-2:]
            except:
                return {"valid": False}
        else:
            entryDict[data[0]] = data[1]
    return entryDict


# Returns true if valid, false otherwise.  Evaluates a single entry (dict)
# Continue to ignore the cid
def validateData(entry):
    # Birth Year (byr)
    if entry["byr"] < 1920 or entry["byr"] > 2002:
        return False
    # Issue Year (iyr)
    if entry["iyr"] < 2010 or entry["iyr"] > 2020:
        return False
    # Expiration Year (eyr)
    if entry["eyr"] < 2020 or entry["eyr"] > 2030:
        return False

    if invalidHeight(entry["hgt"], entry["hgtUnit"]):
        return False

    if invalidHairColor(entry["hcl"]):
        return False

    if entry["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    if invalidPid(entry["pid"]):
        return False
    # No errors detected!
    return True


# Checks the height(hgt) and height unit(hgtUnit)
# Returns True if an error was detected, False if correct.
def invalidHeight(height, unit):
    if unit not in ["in", "cm"]:
        return True

    if unit == "cm":
        if height < 150 or height > 193:
            return True
        else:
            return False

    elif unit == "in":
        if height < 59 or height > 76:
            return True
        else:
            return False


# Checks the passport ID. (pid)
# Returns True if an error was detected, False if correct.
def invalidPid(originalValue):
    # Check if it is a 9-digit number
    if len(originalValue) != 9:
        return True
    try:
        int(originalValue)
        return False
    except:
        return True


# This just checks the hair color since it requires more detail.
# Returns True if an error was detected, False if correct.
def invalidHairColor(originalValue):
    if originalValue[0] != "#":
        return True
    value = originalValue[1:]
    if len(value) != 6:
        return True
    for _ in value:
        if _ not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]:
            return True
    # Passed all the tests!
    return False


if __name__ == "__main__":
    main()


# Old read code... this was not be processing all the data unless there is a new line
'''
    # split by groupings and delimit by spaces
    entry = ""
    for _ in input:
        line = _.rstrip()
        if line == "":
            data.append(entry)
            entry = ""
        else:
            if entry != "":
                line = " " + line
            entry += line
'''
