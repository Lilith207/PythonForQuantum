import numpy.linalg as npL
import numpy.matrixlib as npM
import numpy as np
import qiskit as QS

QBnum = 1
qc = QS.QuantumCircuit(QBnum)

qc.y(0)
qc.h(0)
vec = QS.quantum_info.Statevector(qc)
print(vec)
print(qc)