import sys
import mmap
import thread
from itertools import permutations
import multiprocessing 


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


if __name__ == '__main__':
    jobs = []
    for x in range (6,10):
        p = multiprocessing.Process(target=lookForWords, args=(x,"dictionary"+str(x)+".txt"))
        jobs.append(p)
        p.start()

