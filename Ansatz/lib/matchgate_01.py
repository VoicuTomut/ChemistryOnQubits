#Useful function to creat matcggate circuit gates#

############################################################################################################################

from lib.const import *
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister 
from qiskit import Aer, execute
from qiskit.quantum_info.operators import Operator

############################################################################################################################

import numpy as np

############################################################################################################################
# We use these funcion to test if our 4x4 matrix are matchgate matrix.
def Match_gate_test(matrice):
    if matrice[0][1]!=0 or matrice[0][2]!=0 or matrice[1][0]!=0 or matrice[1][3]!=0 or matrice[2][0]!=0 or matrice[2][3]!=0 or matrice[3][1]!=0 or matrice[3][2]!=0 :
        print("Zero")
        return 0
    else:
        if (matrice[1][1]*matrice[2][2]-matrice[1][2]*matrice[2][1])==(matrice[0][0]*matrice[3][3]-matrice[0][3]*matrice[3][0]):
            return 1
        else:
            print("det(A)!= det(B)")
            return 0
############################################################################################################################

############################################################################################################################
#machgate matrix with the form:
'''
	[1,0,0,0],
    [0,np.sin(self.theta),np.cos(self.theta),0],
    [0,np.cos(self.theta),-1*np.sin(self.theta),0],
    [0,0,0,-1]]
'''
class swap_t:
    def __init__(self,theata):
        self.theta=theata
        self.mat=np.array([[1,0,0,0],
                           [0,np.sin(self.theta),np.cos(self.theta),0],
                           [0,np.cos(self.theta),-1*np.sin(self.theta),0],
                           [0,0,0,-1]])
    def get_p(self):
        print('thet=',self.theta)
        print('math=', self.mat)

#creat matchgate variable gate with the matrix of the form:
'''
	[1,0,0,0],
    [0,np.sin(self.theta),np.cos(self.theta),0],
    [0,np.cos(self.theta),-1*np.sin(self.theta),0],
    [0,0,0,-1]]
'''
def U_t(theta):
    qc=QuantumCircuit(2,name='G_t('+str(theta)+')')
    qc.unitary(swap_t(theta).mat,[0,1])
    return qc.to_gate()

############################################################################################################################
