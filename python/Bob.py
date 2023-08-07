def response(hey_bob):
    # removing whitespace from the front and back
    hey_bob = hey_bob.strip()
    question = False
    yell = False
    # check if empty string
    if hey_bob == "":
        return "Fine. Be that way!"
    # check if string is a question
    if hey_bob[-1] == "?":
        question = True
    # check if yelling
    if hey_bob == hey_bob.upper() and hey_bob != hey_bob.lower():
        yell = True
    # return depending on yell and question
    if yell == True:
        if question == True:
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    # return if question
    if question == True:
        return "Sure."
    # return if anything else
    return "Whatever."
    pass
