import json


def main():
    rules = getData()
    can_contain_gold_count = count_which_can_contain("shiny gold", rules)
    print(
        f"Part one: {can_contain_gold_count} bag colors can hold shiny gold bags.")


# Part one- counts how many total rules(colors) allow for a specified
# bag color can be placed inside of another.
# Requires the rules dict and returns an integer (count).
def count_which_can_contain(color, rules):
    count_bags = 0
    for bag_type in rules.keys():
        # This bag can hold the color directly
        if bag_can_contain(color, rules[bag_type]):
            count_bags += 1
        # Otherwise, search to see if they can be held indirectly (bag-in-bag-in-bag)
        else:
            for bag in rules[bag_type].keys():
                if bag_can_contain(color, rules[bag]):
                    count_bags += 1
                    # This is required to stop checking for multiple instances
                    break
    return count_bags


# This belongs in another function, but for brainstorming
searched_bags = {
    "has_gold": [],  # List all the bags that can in/directly hold gold
    "no_gold": []   # list all the colors that cannot hold gold
}
# So, searched_bags["has_gold"] will eventually contain the final result (colors, len=count)


# Recursion time - need to search sub-bags and track which have been searched
def recursive_bag_search(color, searched_bags, rules, looking_for="shiny gold"):
    # End conditions
    # This might not be needed, actually. (caught by normal process)
    # if rules[color] == {}:
    #   return
    if color in searched_bags["no_gold"] or color in searched_bags["has_gold"]:
        return
    # General case -not yet searchec
    else:
        # This color was not yet searched - check if gold is in here
        if bag_can_contain(looking_for, rules[color]):
            searched_bags["has_gold"].append(color)
            return
        # This color doesn't have gold listed - check deeper
        else:
            for _ in rules[color].keys():
                recursive_bag_search(_, searched_bags, rules)


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
