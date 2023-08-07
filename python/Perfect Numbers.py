def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    factors = set()
    for i in range(1,number):
        if number % i == 0:
            factors.add(i)

    factor_sum = -number

    for i in factors:
        factor_sum = factor_sum + i

    if factor_sum == 0:
        return 'perfect'
    elif factor_sum > 0:
        return 'abundant'
    else:
        return 'deficient'
    # pass
