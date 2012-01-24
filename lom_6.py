__author__ = 'Step'

def SoD(num):
    """
    Returns sum of digits in number num.

    :type num str
    """
    res = 0
    for i in xrange(len(num)):
        res += int(num[i])
    return res


def main():
    num = 1000000000
    for n in xrange(num, num * 2):
        t = str(n)
        if t.count('5') < 2:
            if 30 < SoD(t) < 39:
                if not (n % 29):
                    print "Found! {0} mod 29 == 0\nSum of digits of {0} is {1}".format(n, SoD(t))
                    break

if __name__ == '__main__': main()
