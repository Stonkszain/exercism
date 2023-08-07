def is_armstrong_number(number):
    sum = 0
    number_string = str(number)
    for i in range(len(number_string)):
        sum += (int(number_string[i]) ** len(number_string))
    return sum == number
    # pass
