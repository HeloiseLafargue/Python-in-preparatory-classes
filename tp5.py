import numpy as np

## Systèmes linéaires


def transvecLigne (A,i,j,c):

    A[i] = A[i] + c*A[j]


def permutLigne (A,i,j):

    A1 = np.copy(A[i])
    A2 = np.copy(A[j])
    A[i] = A2
    A[j] = A1


def dilatLigne (A,i,c):

    A[i] = A[i] * c



def systLin(A,B):

    A1 = np.copy(A)
    B1 = np.copy(B)
    n = np.shape(A)[0]

    for j in range (n-1):       # pour les colonnes de 0 à n-2 compris (on ne fait rien à la dernière)

        for i in range (j+1,n):

            c = A1[i,j]/A1[j,j]
            transvecLigne(A1,i,j,-c)
            transvecLigne(B1,i,j,-c)

    for j in range (n-1,0, -1):

        for i in range (0,j):

            c = A1[i,j]/A1[j,j]
            transvecLigne(A1,i,j,-c)
            transvecLigne(B1,i,j,-c)

    for i in range (n):

        c = 1 / A1[i,i]
        dilatLigne(A1,i,c)
        dilatLigne(B1,i,c)

    return B1

A = np.array( [ [10**(-20), 1], [1,1] ] )
B = np.array( [ [1],[2] ] )



def pivot(A,j):
    grand = abs( A[j,j])
    indice = j
    n = np.shape(A)[0]
    for i in range (j+1,n):
        if grand < abs(A[i,j]):
            grand = abs(A[i,j])
            indice = i
    return indice


def systLinPivot(A,B):

    A1 = np.copy(A)
    B1 = np.copy(B)
    n = np.shape(A)[0]

    for j in range (n-1):

        j0 = pivot(A1,j)            #nouveau
        permutLigne(A1,j,j0)        #nouveau

        for i in range (j+1,n):

            c = A1[i,j]/A1[j,j]
            transvecLigne(A1,i,j,-c)
            transvecLigne(B1,i,j,-c)

    for j in range (n-1,0, -1):

        for i in range (0,j):

            c = A1[i,j]/A1[j,j]
            transvecLigne(A1,i,j,-c)
            transvecLigne(B1,i,j,-c)

    for i in range (n):

        c = 1 / A1[i,i]
        dilatLigne(A1,i,c)
        dilatLigne(B1,i,c)

    return B1

def determinant(A):


