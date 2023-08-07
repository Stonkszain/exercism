def equilateral(sides):
    if triangle_integrity_checker(sides):
        if sides[0] == sides[1] == sides[2]:
            return True
    return False
    # pass


def isosceles(sides):
    if triangle_integrity_checker(sides):
        if sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
            return True
    return False
    # pass


def scalene(sides):
    if triangle_integrity_checker(sides):
        if not equilateral(sides) and not isosceles(sides):
            return True
    return False
    # pass

def triangle_integrity_checker(sides):
    if not sides[0] + sides[1] >= sides[2]:
        return False
    if not sides[1] + sides[2] >= sides[0]:
        return False
    if not sides[2] + sides[0] >= sides[1]:
        return False
    if not sides[0] > 0 and not sides[1] > 0 and not sides[2] > 0:
        return False
    return True
