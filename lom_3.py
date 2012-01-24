__author__ = 'Step'

def number_of_divisors(num):
    """
    Returns number of natural divisors of num

    :type num int
    """
    if num < 0:
        raise ValueError
    result = 1
    for pot_div in xrange(1, num/2 + 1):
        if not num % pot_div:
            result += 1
    return result


def main():
    string_divs = ''
    n = 1
    while len(string_divs) < 2022:
        string_divs += str(number_of_divisors(n))
        n += 1
    print string_divs[2011:2021]

if __name__ == '__main__':
    main()
