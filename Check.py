import numpy.linalg as npL
import numpy.matrixlib as npM
import numpy as np
import math

Mat1 = [[0, 1j],[-1j,0]]
Mat2 = [[1,0],[0,1j]]
Mat3 = [[1/math.sqrt(2)],[1/math.sqrt(2)]]
Mat4 = [[0],[2j]]

print(npM.asmatrix(Mat1))
print(npM.asmatrix(Mat2))
print(npM.asmatrix(Mat3))
print(npM.asmatrix(Mat4))

print("test")