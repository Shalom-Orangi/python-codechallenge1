def only_two_positive_integers(a, b, c):
    count = 0

    if a > 0:
        count += 1
    if b > 0:
        count += 1
    if c > 0:
        count += 1

    return count == 2

print(only_two_positive_integers(4,6,10))
#this function only returns True when there are only two,positive integers. not more, not less.