## TP 2 : ALGORITHMES DE TRI



# Tri bulle

def unePasse(l,d):
    """entrée : liste l et indice du dernier élément d
    sortie : True si on modifie la liste, False sinon"""
    test = False
    for i in range (d) :
        if l[i] > l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
            test = True
    return test


def triBulle1(l):
    n = len(l)
    for i in range (n-1,0,-1):
        unePasse(l,i)


def triBulle2(l):
    """entrée : liste l
    sortie : ne renvoit rien
    La fonction trie la liste et si l ou une de ses sous-listes étaient triées la fonction s'arrête """
    non_trie = True
    d = len(n) - 1
    while non_trie :
            non_trie = unePasse(l,d)
            d = d-1



# Tri par dénombrement

def occurrences(l,d):
    """entrée : liste l et entier d
    sortie : retourne une liste contenant le nombre d'ocurrences de l'entier k appartenant à [0,d-1], dans la liste l"""
    occ = [0]*d
    for e in l:
        occ[ e ] += 1
    return occ


def modifie(occ):
    for k in range (1,len(occ)):
        occ[k] += occ[k-1]


def triDenom(l,d) :
    res = [0]*len(l)
    occ = occurrences(l,d)
    modifie( occ )
    for e in l :
        res[ occ[e]-1 ] = e
        occ[e] -= 1
    return res
