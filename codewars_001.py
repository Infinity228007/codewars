def narcissistic(value):
    digits = [int(num) for num in str(value)]
    n = len(digits)
    if sum([num**n for num in digits]) == value:
        return True
    else:
        return False  # Code away


narcissistic(7)
narcissistic(371)
narcissistic(122)
narcissistic(4887)
