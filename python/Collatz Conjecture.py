def steps(number):
    if ( number < 1):
        # example when argument is zero or a negative integer
        raise ValueError("Only positive integers are allowed")
    step_counter = 0
    while ( number != 1 ):
        if ( number % 2 == 0 ):
            number = number / 2
            step_counter += 1
        elif ( number % 2 == 1 ):
            number = ( number * 3 ) + 1
            step_counter += 1
    return step_counter
    # pass
