def translate(text):
    sentence_list = text.split()

    sentence = ''
    counter = 0

    for word in sentence_list:
        if counter > 0:
            sentence = sentence + ' '
        sentence = sentence + translate_word(word)
        counter += 1

    return sentence

def translate_word(text):
    text = text.lower()
    first_letter = text[0]
    first_two = text[0:2]
    second_letter = text[1]
    if len(text) > 2:
        first_three = text[0:3]
        second_two = text[1:3]
        third_letter = text[2]
    else:
        first_three = ''
        second_two = ''
        third_letter = ''
    if first_letter in ('a', 'e', 'i', 'o', 'u'):
        text = text + "ay"
    elif first_two in ('yt', 'xr'):
        text = text + "ay"
    elif first_three in ('sch', 'thr'):
        text = text[3:] + first_three + "ay"
    elif first_two in ('qu', 'ch', 'th'):
        text = text[2:] + first_two + "ay"
    elif second_two == 'qu':
        text = text[3:] + first_three + "ay"
    elif second_letter == 'y':
        text = text[1:] + first_letter + "ay"
    elif third_letter == 'y':
        text = text[2:] + first_two + "ay"
    else:
        text = text[1:] + first_letter + "ay"
    return text
    # pass
