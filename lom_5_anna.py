# -*- coding: UTF-8 -*-
__author__ = 'Step'

def main(anna):
    """
    What can i say here?
    This code simply opens original text (11), reads it (12), divides into separate words (14-15),
    finds words consisting of 4 letters (20-22), changes all 'ё' and 'Ё' to 'е', lowers all words, and counts them (24-30)
    then sorts them by frequency.
    Output is saved in 'anna-out.txt', without lexicographical sorting, which I've done by myself.

    :type anna string
    """
    from urllib2 import urlopen
    import re

    f = urlopen(anna)
    anna = unicode(f.read(), 'utf8')
    f.close()
    regexp = re.compile(ur'\W', re.U)
    dictionary_temp = regexp.split(anna)
    words4_temp = []
    freq_dict = {}
    words4_temp = filter(dictionary_temp, lambda x: len(x) == 4)
    del dictionary_temp
    yo_regex = re.compile(ur'[\u0401\u0451]')
    for word in words4_temp:
        word = yo_regex.sub(ur'\u0435', word).lower()
        try:
            freq_dict[word] += 1
        except KeyError:
            freq_dict[word] = 1
    del words4_temp
    freq_dict = list(freq_dict.viewitems())
    freq_dict = sorted(freq_dict, key=lambda word: word[1])
    freq_dict.reverse()
    f = open('anna_out.txt', 'w')
    writeout = ''
    for i, word in enumerate(freq_dict):
        writeout += '{0}. {1} - {2} упоминаний.\n'.format(i + 1, word[0].encode('utf-8'), word[1])
    f.write(writeout)
    f.close()
    print 'Success! Open anna_out.txt'

if __name__ == '__main__':
    anna = 'http://ejudge.ru/study/anna.txt'
    main(anna)
