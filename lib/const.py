#Just a lib from some constants#

import numpy as np

# Pauli matrix
I=np.array([[1,0],[0,1]],dtype=np.complex128)
X=np.array([[0,1],[1,0]],dtype=np.complex128)
Y=np.array([[0,-1.0j],[1.0j,0]],dtype=np.complex128)
Z=np.array([[1,0],[0,-1]],dtype=np.complex128)

# Zero and One
Z0=np.array([1,0])
U1=np.array([0,1])