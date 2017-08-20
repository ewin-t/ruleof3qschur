# Schur-Q Reading in hook order
# Intended to be pasted into sage's interactive interface
import itertools as itr
#A.<w,x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
A.<x,y> = FreeAlgebra(QQ, implementation='letterplace')
def get_hks(k, s):
    if k == 0:
        return 1
    f = 0
    for i in itr.combinations_with_replacement(s, k):
        monomial = 1
        for j in i:
            monomial = monomial * j
        f += monomial
    return f

def get_eks(k, s):
    if k == 0:
        return 1
    f = 0
    for i in itr.combinations(s, k):
        monomial = 1
        for j in i:
            monomial = monomial * j
        f += monomial
    return f

def get_qks(k, s):
    f = 0
    for i in range(0, k+1):
        f += get_eks(i, s[::-1]) * get_hks(k-i, s)
    return f

#subsets = list(itr.chain.from_iterable(itr.combinations((w,x,y,z), r) for r in range(1,5)))
subsets = ([x,y])
q1s = [get_qks(1, s) for s in subsets]
q3s = [get_qks(3, s) for s in subsets]
q5s = [get_qks(5, s) for s in subsets]
q7s = [get_qks(7, s) for s in subsets]

relations = []
for i in range(0, len(subsets) - 1):
    relations.append(q1s[i]*q3s[i]-q3s[i]*q1s[i])
    relations.append(q1s[i]*q5s[i]-q5s[i]*q1s[i])
    relations.append(q1s[i]*q7s[i]-q7s[i]*q1s[i])

I = A * relations * A

q7 = get_qks(7, (x,y,z))
test = q1s[0] * q7 - q7 * q1s[0]
test in I
