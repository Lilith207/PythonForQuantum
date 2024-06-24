import itertools

print(list(itertools.permutations(range(4))))
Iters = list(itertools.permutations(range(4)))

numbs = (
    (0,1,2,2),
    (0,3,1,1),
    (0,3,3,0),
    (0,1,2,3),
    (0,3,0,2),
    (0,3,0,1)
)

for i in Iters:
    strs = ""
    for p in numbs:
        one   = i[p[0]]
        two   = i[p[1]]
        three = i[p[2]]
        four  = i[p[3]]
        #total = one*4**3 + two*4**2 + three*4**1 + four*4**0
        total = one*10**3 + two*10**2 + three*10**1 + four*10**0
        strs += chr(total)
        #print(total)
    print(strs)