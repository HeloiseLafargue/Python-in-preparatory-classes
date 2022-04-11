## TP 4 : RECURSIVITE

import numpy as np


# Suite de Fibonacci

def puissMat(A,n):

    if n ==0 :
        return np.array( [[1,0],[0,1]] )

    if n%2 == 0 :
        return( puissMat( np.dot(A,A) ,n//2) )

    B = puissMat(np.dot(A,A),n//2)
    return( np.dot(A,B) )


def fibo(n) :

    A = np.array( [[0,1],[1,1]] )
    U = puissMat(A,n)
    return U[0,1]



# Fractions continues

def fractionContinue(p,q) :

    if p%q == 0 :
        return [p//q]

    l = fractionContinue(q,p%q)
    a0 = p//q
    l.append(a0)
    return l


def recompose(l) :

    if len(l) == 1 :
        return (l[0], 1)

    p1,q1 = recompose( l[:-1] )
    return ( p1*l[-1]+q1, p1)


# Le compte est bon

def decomposable(s,l):
    if s == 0 :
        return True
    if len(l) == 0 :
        return False
    if s < l[-1] :
        return decomposable(s,l[:-1])
    return decomposable( s-l[-1], l[:-1]) or decomposable(s,l[:-1])
