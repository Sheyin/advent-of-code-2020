import json

gold = "shiny gold"
searched_bags = {
    "has_gold": [],  # List all the bags that can in/directly hold gold
    "no_gold": []   # list all the colors that cannot hold gold
}
rules = {}


def main():
    global rules
    rules = getData()
    search_bags_for_gold()
    print(
        f'Part one: {len(searched_bags["has_gold"])} bags can eventually hold {gold} bags.')


# This just populates the searched_bags dict with the
# search results whether it can hold gold bags (sorting function)
def search_bags_for_gold():
    # Populate searched bags with initial top level results
    # Before calling recursive function
    for color in rules.keys():
        if bag_can_contain(gold, rules[color]):
            searched_bags["has_gold"].append(color)
    # Run loop again but lets just search for everything
    # I'm sure this is probably not quite correct.
    for color in rules.keys():
        search_bags_for_color(color)


# Recursive function - searches if a bag can eventually hold gold
# Mostly just to populate searched_bags and sort the results.
def search_bags_for_color(color):
    if color in searched_bags["has_gold"]:
        return True
    elif color in searched_bags["no_gold"]:
        return False
    else:
        for sub_color in rules[color].keys():
            if search_bags_for_color(sub_color):
                searched_bags["has_gold"].append(color)
                return True
        # Searched all bags for colors - not found among sub colors
        searched_bags["no_gold"].append(color)
        return False


# Helper function that looks in a rule for a specific color (dict) and looks
# to see if a specified color can be placed inside.
# Returns True if it can, False otherwise
def bag_can_contain(color, rule):
    if color in rule.keys():
        return True
    else:
        return False


# Read data, format as dictionary-in-dictionary w/ colors as keys, return dict
def getData():
    # Get file input
    #filename = "./data/" + "day7testinput.txt"
    filename = "./data/" + "day7input.txt"
    raw_input = []
    rules = {}
    input = open(filename, "r")

    for _ in input:
        line = _.rstrip()
        raw_input.append(line)
        color_key_index = line.find(" bags contain ")
        color_key = line[:color_key_index]
        rules[color_key] = {}

        # Getting data portion of line: color_key_index + 14 (" bags contain ")
        remaining_line = line[color_key_index + 14:]
        bags_contained_dict = {}

        if remaining_line == "no other bags.":
            continue
        else:
            remaining_split = remaining_line.split(", ")
            for _ in remaining_split:
                stop_point = _.find(" bag")
                quantity = _[0]
                bag_type = _[2:stop_point]
                bags_contained_dict[bag_type] = quantity
        rules[color_key] = bags_contained_dict
    return rules
    # printDict(rules)


# Just for testing, really.  Prints contents of dict in json format
def printDict(dict):
    print(json.dumps(dict, indent=4))


if __name__ == "__main__":
    main()
