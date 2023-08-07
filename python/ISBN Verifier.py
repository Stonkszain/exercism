def is_valid(isbn):
    isbn = isbn.replace('-','')

    ten = []
    
    for i in range(10):
        ten.append(str(i))
    
    for i in isbn:
        if i not in ten:
            if i != 'X':
                return False
    
    if len(isbn) != 10:
        return False
    
    
    sum = 0
    
    for i in range(10):
        if isbn[i] == 'X' and i == 9:
            sum = sum + 10 * (10 - i)
        elif isbn[i] == 'X':
            return False
        else:
            sum = sum + (int(isbn[i]) * (10 - i))

    if sum % 11 == 0:
        return True
    return False
    pass
