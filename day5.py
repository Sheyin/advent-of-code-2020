F = "F"
R = "R"
L = "L"
B = "B"


def main():
    # Get file input
    filename = "./data/day5input.txt"
    input = open(filename, "r")
    boarding_passes = []

    for _ in input:
        line = _.rstrip()
        boarding_passes.append(line)
        # There are 128 rows, ranging from 0 to 127

    # boarding_passes should now be a tidy array of data
    # Initial range
    range = (1, 128)
    # This is the example given on the website.  Using it to debuf splitSeat()
    boarding_pass = "FBFBBFFRLR"
    for char in boarding_pass:
        range = splitSeat(char, range)
        print(f'{char}: {range}')


# For part 1 - calculates the seat's row/col position based on rules.
# Returns an integer (hopefully, the seat location)
# There are 128 rows, ranging from 0 to 127 - F/B used to calculate
# F: lower half
# B: upper half
# Last 3 chars will be L/R to calculate column #, but ranging from 0-7 (8 total)
# L: lower half
# R: upper half
def locateSeat(boarding_pass):
    for _ in boarding_pass:
        pass


# Helper function for locateSeat.
# Splits maxSeat(highest row/col) based on letter
# Expects a tuple of (lowestPossibleSeat, highestPossibleSeat)
# Returns resulting tuple of new min/max possible positions
def splitSeat(letter, range):
    minSeat = range[0]
    maxSeat = range[1]
    # Keep upper half
    if letter == "B" or letter == "R":
        newMinSeat = int(maxSeat / 2)
        #print("newMinseat: " + str(newMinSeat))
        return (newMinSeat, maxSeat)
    # Keep lower half
    # elif letter == "F" or letter == "L":
    else:
        newMaxSeat = int(minSeat + maxSeat / 2)
        #print("newMaxseat: " + str(newMaxSeat))
        return (minSeat, newMaxSeat)
    '''
    else:
        print("Some error occurred - neither F/B/L/R")
    '''


if __name__ == "__main__":
    main()
