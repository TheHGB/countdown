import sys
from itertools import permutations
import multiprocessing 


word = sys.argv[1]


def lookForWords(length, dictionary):
    global word
    anagrams = set([''.join(w) for w in permutations(word,length)])

    f = open(dictionary)
    text = f.read().strip().split()
    words = set(text) & anagrams
    print str(length)+":"+str(list(words))

if __name__ == '__main__':
    jobs = []
    for x in range (6,10):
        p = multiprocessing.Process(target=lookForWords, args=(x,"dictionary"+str(x)+".txt"))
        jobs.append(p)
        p.start()

