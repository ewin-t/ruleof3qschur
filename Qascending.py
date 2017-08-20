# Schur Q-polynomials, reading in ascending order
# Confirming that the relations given imply the relations for test.
A.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
q1 = x+y+z
q1a = y+z
q1b = x+z
q1c = x+y

q3 = z^3+y^3+x^3+2*(x^2*z+x*z^2+x^2*y+x*y^2+y^2*z+y*z^2)+4*x*y*z
q3a = z^3+y^3+2*(y*y*z+y*z*z)
q3b = z^3+x^3+2*(x*x*z+x*z*z)
q3c = y^3+x^3+2*(x*x*y+x*y*y)

q5 = z^5+y^5+x^5+2*(y^4*z+y^3*z^2+y^2*z^3+y*z^4+x^4*y+x^3*y^2+x^2*y^3+x*y^4+x^4*z+x^3*z^2+x^2*z^3+x*z^4)+4*(x^3*y*z+x*y^3*z+x*y*z^3+x^2*y^2*z+x^2*y*z^2+x*y^2*z^2)
q5a = z^5+y^5+2*(y^4*z+y^3*z^2+y^2*z^3+y*z^4)
q5b = z^5+x^5+2*(x^4*z+x^3*z^2+x^2*z^3+x*z^4)
q5c = x^5+y^5+2*(x^4*y+x^3*y^2+x^2*y^3+x*y^4)

q7 = 2*x^7 + 4*x^6*y + 4*x^5*y^2 + 4*x^4*y^3 + 4*x^3*y^4 + 4*x^2*y^5 + 4*x*y^6 + 2*y^7 + 4*x^6*z + 8*x^5*y*z + 8*x^4*y^2*z + 8*x^3*y^3*z + 8*x^2*y^4*z + 8*x*y^5*z + 4*y^6*z + 4*x^5*z^2 + 8*x^4*y*z^2 + 8*x^3*y^2*z^2 + 8*x^2*y^3*z^2 + 8*x*y^4*z^2 + 4*y^5*z^2 + 4*x^4*z^3 + 8*x^3*y*z^3 + 8*x^2*y^2*z^3 + 8*x*y^3*z^3 + 4*y^4*z^3 + 4*x^3*z^4 + 8*x^2*y*z^4 + 8*x*y^2*z^4 + 4*y^3*z^4 + 4*x^2*z^5 + 8*x*y*z^5 + 4*y^2*z^5 + 4*x*z^6 + 4*y*z^6 + 2*z^7
q7a = 2*y^7 + 4*y^6*z + 4*y^5*z^2 + 4*y^4*z^3 + 4*y^3*z^4 + 4*y^2*z^5 + 4*y*z^6 + 2*z^7
q7b = 2*x^7 + 4*x^6*z + 4*x^5*z^2 + 4*x^4*z^3 + 4*x^3*z^4 + 4*x^2*z^5 + 4*x*z^6 + 2*z^7
q7c = 2*x^7 + 4*x^6*y + 4*x^5*y^2 + 4*x^4*y^3 + 4*x^3*y^4 + 4*x^2*y^5 + 4*x*y^6 + 2*y^7

test = q5*q3 - q3*q5
relations = [q3a*q1a - q1a*q3a, q3b*q1b - q1b*q3b, q3c*q1c - q1c*q3c, q3*q1 - q1*q3, q5a*q1a - q1a*q5a, q5b*q1b - q1b*q5b, q5c*q1c - q1c*q5c, q1*q5-q5*q1, q1*q7-q7*q1, q1a*q7a-q7a*q1a, q1b*q7b-q7b*q1b, q1c*q7c-q7c*q1c]
I = A*relations*A
print (test in I)
