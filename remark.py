# We try to generalize the conjecture to nonspecific as, bs, As, and Bs
# Because these relations are not enough to give the result, we are missing relations given by setting these variables to the generating functions as in the statement of the conjecture for Schur Q-functions.

A.<a1,a2,b1,b2,A1,A2,B1,B2> = FreeAlgebra(QQ, implementation='letterplace')
ones = [a1, b1, A1, B1] # as and bs
twos = [a2, b2, A2, B2] # alphas and betas
relations = []
for i,j in itr.combinations(range(4), 2):
    relations.append(ones[i]*ones[j]-ones[j]*ones[i])
    relations.append(twos[i]*twos[j]-twos[j]*twos[i])
relations.append((a1 * A2 - A2 * a1) - (a2 * A1 - A1 * a2))
relations.append((a1 + a2)*A2*A1*B1*B2 - A2*A1*B1*B2*(a1 + a2))
relations.append((A1 + A2)*a2*a1*b1*b2 - a2*a1*b1*b2*(A1 + A2))

a2*a1*b1*b2*A2*A1*B1*B2 - A2*A1*B1*B2*a2*a1*b1*b2 in I
