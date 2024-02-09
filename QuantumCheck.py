import numpy.linalg as npL
import numpy.matrixlib as npM
import numpy as np
import qiskit as QS
import qiskit_ibm_runtime as QSR
import math

#service = QSR.QiskitRuntimeService()

QBnum = 1
qc = QS.QuantumCircuit(QBnum)

qc.h(0)

qc.draw()