from itertools import permutations
import enchant
d=enchant.Dict("en_US")

text=input()
letter=[x.lower() for x in text]
#print(letter)
words=set()
#print(list(permutations(letter)))
for n in range(len(text)):
    for i in list(permutations(letter,n+1)):
        k=("".join(i))
        if len(k)>2:
            if d.check(k):
                words.add(k)

print(words)
