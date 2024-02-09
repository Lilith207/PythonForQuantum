import numpy.linalg as npL
import numpy.matrixlib as npM
import numpy as np
import qiskit as QS
import qiskit_ibm_runtime as QSR
import math

Mat1 = [[0, 1j],[-1j,0]]
Mat2 = [[1,0],[0,1j]]
Mat3 = [[1/math.sqrt(2)],[1/math.sqrt(2)]]
Mat4 = [[0],[2j]]

sav = np.array(Mat1)

print(sav)
#print(npM.asmatrix(Mat2))
#print(npM.asmatrix(Mat3))
#print(npM.asmatrix(Mat4))

#print("test")