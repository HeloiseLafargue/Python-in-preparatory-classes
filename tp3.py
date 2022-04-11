## TP 3 : RECURSIVITE

#1
def f(n) :
    if n == 0 :
        return (1)
    u = f(n-1)                          # calculer u avant pour ne pas le recalculer 2 fois !!
    return (1/2)*(u + 2/u )


#2
def positifs(l) :
    if len(l) == 0 :
        return []
    liste = positifs(l[:-1])
    if l[-1] >= 0 :
        liste.append(l[-1])
    return liste


#3
def evalue(l,x) :
    if len(l) == 0 :
        return 0
    return evalue( l[0] + l[1:]*x )


#4
def chercheEntre(a,b,n) :
    if (b-a) <= 1 :
        return a
    m = (a+b)//2
    if n == m*m :
        return m
    if m*m > n :
        return chercheEntre(a,m,n)
    return chercheEntre(m,b,n)

def racineEntiere(n) :
    a = 0
    b = n + 1
    return chercheEntre(a,b,n)



#5
def numero(x,y) :
    if (x,y) == (0,0):
        return 0
    if x == 0 :
        return numero(x+1,y-1) + 1          #inutile
    if y == 0 :
        return numero(y,x-1) + 1
    else :
        return numero(x+1,y-1) + 1

def point(n) :
    (x,y) = point(n-1)
    if x == 0 :
        return (0,y+1)
    if y == 0 :
        return (x-1,y+1)                    #inutile
    else :
        return(x-1,y+1)

