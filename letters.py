import sys
import mmap
import thread
from itertools import permutations

word = sys.argv[1]


def lookForWords(length, dictionary):
    global word
    anagrams = []
    anagrams = list(set([''.join(w) for w in permutations(word,length)]))

    f = open(dictionary)
    text = f.read().strip().split()
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    for word in anagrams:
        if word in text:
            print str(length) + ":" + word


try:
    thread.start_new_thread (lookForWords, (6,"dictionary6.txt") )
    thread.start_new_thread (lookForWords, (7,"dictionary7.txt") )
    thread.start_new_thread (lookForWords, (8,"dictionary8.txt") )
    thread.start_new_thread (lookForWords, (9,"dictionary9.txt") )
except:
    print "nope"
while 1:
    pass
