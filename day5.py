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
    # boarding_passes should now be a tidy array of data

    highest_seat_pid = 0
    for boarding_pass in boarding_passes:
        seat_info = {}
        seat = locateSeat(boarding_pass)
        seat_info["row"] = seat[0]
        seat_info["col"] = seat[1]
        seat_info["pid"] = (seat[0] * 8) + seat[1]
        seat_info["pattern"] = boarding_pass
        if seat_info["pid"] > highest_seat_pid:
            highest_seat_pid = seat_info["pid"]
    print(f"Part One: Highest Seat PID is: {highest_seat_pid}")


# Calculates the seat's row/col position based on rules.
# Return a tuple (row, column)
def locateSeat(boarding_pass):
    row_pattern = boarding_pass[:-3]
    col_pattern = boarding_pass[-3:]
    row_range = (0, 127)
    for char in row_pattern:
        row_range = splitSeat(char, row_range)
    col_range = (0, 7)
    for char in col_pattern:
        col_range = splitSeat(char, col_range)
    return (row_range[0], col_range[0])


# Helper function for locateSeat.
# Splits maxSeat(highest row/col) based on letter
# Expects a tuple of (lowestPossibleSeat, highestPossibleSeat)
# Returns resulting tuple of new min/max possible positions
def splitSeat(letter, range):
    minSeat = range[0]
    maxSeat = range[1]
    difference = int((maxSeat - minSeat) / 2)
    lowerHalf = (minSeat, minSeat + difference)
    upperHalf = (maxSeat - difference, maxSeat)

    # Keep upper half
    if letter == "B" or letter == "R":
        return upperHalf
    # Keep lower half
    elif letter == "F" or letter == "L":
        return lowerHalf
    else:
        print("Some error occurred - neither F/B/L/R")


if __name__ == "__main__":
    main()
