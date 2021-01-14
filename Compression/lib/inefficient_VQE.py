#Inefficient matchgate VQE#

#############################################################################################################################

from lib.matchgate_01 import *
from lib.expected import expected

#############################################################################################################################

import numpy as np

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister 
from qiskit import Aer, execute
from qiskit.quantum_info.operators import Operator

#############################################################################################################################
#Exact solver for reference:
def Exact_solver(qubitOp):
    ex = NumPyEigensolver(qubitOp)
    result = ex.run()
    ref = result['eigenvalues']
    return np.real(ref)[0]

#############################################################################################################################
#All the elements needed to assemble the VQE
def ansatz_cell(qc,qo,nr_o, nr_e,thetas):
    
    #qo=QuantumRegister(nr_o,'qo')
    #qc=QuantumCircuit(qo,name='ansatz_cell')
    
    it=iter(thetas)
    start=nr_e-1
    limit=nr_o
    while start!=-1:
        cq=start
        tq=start+1
        while tq<limit:
            qc.append(U_t(next(it)),[cq,tq])
            cq=cq+1
            tq=tq+1

        start=start-1
        limit=limit-1
    return qc 

def var_circ(nr_o,nr_e,theta):
    qo=QuantumRegister(nr_o,'qo')
    cb=ClassicalRegister(nr_o,'cl')
    circ = QuantumCircuit(qo,cb)
    for i in range(nr_e):
        circ.x(i)
    ansatz_cell(circ,qo,nr_o, nr_e,theta)
    return circ

# Caluclate final expected value as sum of h[i]<psi|h_obs|psi> where h_obs-> h_label[i].

def value(h,h_label,circ,backend):
    
    val=0
    for i in range(len(h)):
        if h[i]!=0:
            exp=expected(circ,h_label[i],shots=100000,backend=backend)
            val=val+h[i]*exp
            #print('exp for {} ={}'.format(h_label[i],exp))
            
    return (val)


def cost(theta,weight,pauli,nr_o,nr_e,backend):
    circ=var_circ(nr_o,nr_e,theta)
    return value(weight,pauli,circ,backend)
#############################################################################################################################