import numpy.linalg as npL
import numpy.matrixlib as npM
import numpy as np
import qiskit as QS

QBnum = 1
qc = QS.QuantumCircuit(QBnum)

qc.x(0)
print(QS.quantum_info.Statevector(qc))

print(QS.quantum_info.Statevector(qc))
qc.h(0)
qc.y(0)
print(QS.quantum_info.Statevector(qc))
print(qc)