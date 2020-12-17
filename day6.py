def main():
    # Get file input
    filename = "./data/day" + "6" + "input.txt"
    #filename = "./data/day" + "6" + "testinput.txt"
    input = open(filename, "r")
    raw_data = input.read()

    group_data = raw_data.split("\n\n")
    sorted_data = []

# Each letter (input) = a question, each line = a person, each spaced group of text = a group
# Separate each group into a list of groups?
    for _ in group_data:
        sorted_data.append(_.split('\n'))

    sumOfQuestions = 0
    sumOfQuestionsAllAnswered = 0
    for group in sorted_data:
        sumOfQuestions += countQuestions(group)
        sumOfQuestionsAllAnswered += countQuestionsAllYes(group)

    print(f'Part One: The sum of the yes-questions is: {sumOfQuestions}')
    print(
        f'Part Two: The sum of the yes-questions everyone answered is: {sumOfQuestionsAllAnswered}')


# This is for part 1 - could the questions and return the sum of the questions
# for which a yes was answered
def countQuestions(group):
    uniqueQuestions = []
    for person_answers in group:
        for question in person_answers:
            if question not in uniqueQuestions and question != "\n":
                uniqueQuestions.append(question)
    return len(uniqueQuestions)


def countQuestionsAllYes(group):
    uniqueQuestions = {}
    sizeOfGroup = len(group)
    for person_answers in group:
        for question in person_answers:
            if question not in uniqueQuestions.keys() and question != "\n":
                uniqueQuestions[question] = 1
            elif question in uniqueQuestions.keys():
                uniqueQuestions[question] += 1

    # Figure out which questions everyone answered 'yes' to
    # ignore ones w/out full participation
    uniqueQuestionCount = 0
    for field in uniqueQuestions.keys():
        if uniqueQuestions[field] == sizeOfGroup:
            uniqueQuestionCount += 1

    return uniqueQuestionCount


if __name__ == "__main__":
    main()
