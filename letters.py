import sys
import mmap
from itertools import permutations

word = sys.argv[1]
anagrams = []

for x in range(4,len(word)):
    anagrams = anagrams + list(set([''.join(w) for w in permutations(word,x+1)]))

f = open('dictionary.txt')
text = f.read().strip().split()
s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
for word in anagrams:
    if word in text:
        print word
