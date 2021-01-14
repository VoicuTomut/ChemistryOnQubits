#Useful math operations#

############################################################################################################################

from lib.const import *

############################################################################################################################

import numpy as np
import itertools 

############################################################################################################################

pauli=[I,X,Y,Z]
labels=['I','X','Y','Z']
indice=[0,1,2,3]

############################################################################################################################
# Make Hilbert Schmid product betwen matrices mat1 and mat2
def HS(mat1,mat2): 
    return(np.dot(mat1.conjugate().transpose(), mat2)).trace()

############################################################################################################################

############################################################################################################################
#Pauli decomposition:
# Decompose  observable in matrices create by kron. product o Pauli matrices (h-coeficient , h_label-kron product structure )
def decompose(O):
    size=len(O)
    nr_pauli=np.log2(size)
    norm_fact=1/(2**nr_pauli)

    elements=itertools.product(indice,repeat=int(nr_pauli))
    h_label=[]
    h=[]
    for i in elements:
        label=''
        matrice=pauli[i[0]]
        for  j in i :
            label=label+labels[indice[j]]
        for j in range(int(nr_pauli)-1):
            matrice=np.kron(matrice,pauli[i[j+1]])
        #print(matrice)
        h_label.append(label)
        h.append(norm_fact*HS(matrice,O))

    return h,h_label

def print_decompose(mat):
    c,l=decompose(mat)
    for i in range(len(l)):
        if(abs(c[i])>=0.00000000001):
            print('{}:{}'.format(l[i],c[i])) 

############################################################################################################################