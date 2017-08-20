# Loop symmetric polynomials
# We consider three flavors and three variables
# Relations between e1s and e2s, and e1s and e3s, do not imply e2s and e3s.

import itertools as itr
A.<a1,a2,a3,b1,b2,b3,c1,c2,c3> = FreeAlgebra(QQ, implementation='letterplace')
As = (a1,a2,a3)
Bs = (b1,b2,b3)
Cs = (c1,c2,c3)

def get_eks(k, s, flavor):
    if k == 0:
        return 1
    final = 0
    for i in itr.combinations(s, k):
        f = flavor
        monomial = 1
        for j in i:
            monomial = monomial * j[f]
            f = (f + 1) % len(s[0])
        final += monomial
    return final
subsets = ((As,Bs,Cs),(As,Bs),(As,Cs),(Bs,Cs))
e1s = [[get_eks(1, s, f) for f in range(3)] for s in subsets]
e2s = [[get_eks(2, s, f) for f in range(3)] for s in subsets]
e3s = [[get_eks(3, s, f) for f in range(3)] for s in subsets]
relations = []
for i in range(4):
    for c in itr.product(range(3),repeat=2):
        relations.append(e1s[i][c[0]]*e2s[i][c[1]] - e2s[i][c[0]]*e1s[i][c[1]])
        relations.append(e1s[i][c[0]]*e3s[i][c[1]] - e3s[i][c[0]]*e1s[i][c[1]])
I = A * relations * A
