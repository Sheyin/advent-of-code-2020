def main():
    # Get file input
    filename = "./data/day" + "4" + "input.txt"
    input = open(filename, "r")
    data = []
    raw_data = input.read()
    data = raw_data.split("\n\n")
    print(len(data))

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

    validCount = 0
    for _ in data:
        validPassport = checkFields(_, partOneRequiredFields)
        if validPassport:
            validCount += 1
    print(f'Valid passports: {validCount} / Total Entries: {len(data)}')


def checkFields(entry, fieldsDict):
    requiredFields = fieldsDict.keys()
    for field in requiredFields:
        if field not in entry and fieldsDict[field] == True:
            return False
    return True


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
