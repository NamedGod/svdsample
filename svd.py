## Based on 2.3 of OFFLINE BILINGUAL WORD VECTORS, 
## ORTHOGONAL TRANSFORMATIONS AND THE INVERTED SOFTMAX 
## (https://openreview.net/pdf?id=r1Aab85gg)

import numpy as np
import scipy.linalg as linalg

COLS = 5
ROWS = 50

def subtractMean(matrix):
	duplicate = matrix;
	for i in range(COLS):
		sumOfCol = 0
		for j in range(ROWS):
			sumOfCol += matrix[j][i]
		sumOfCol /= ROWS
		for j in range(ROWS):
			duplicate[j][i] -= sumOfCol
	return duplicate


X = np.loadtxt("testmatrix1.txt")
Y = np.loadtxt("testmatrix2.txt")

# Random rotating matrix
M_rotate = np.array([[-0.44397795,  0.2671975 , -0.6733675 ,  0.29900409, -0.43435221],
       [-0.50094984, -0.35522826,  0.4676279 ,  0.63572622,  0.00620209],
       [-0.38569981,  0.2544876 , -0.20820321, -0.01698669,  0.86187853],
       [-0.44778648, -0.65050932, -0.18073076, -0.5827816 , -0.06345774],
       [-0.45017305,  0.56079592,  0.50188462, -0.40807571, -0.25384682]])

Y = np.dot(Y, M_rotate)

XDprime = subtractMean(X)
YDprime = subtractMean(Y)

Q_D, Sigma_X, V_X_T = linalg.svd(XDprime, full_matrices = False)
V_X = np.transpose(V_X_T)
W_D, Sigma_Y, V_Y_T = linalg.svd(YDprime, full_matrices = False)
V_Y = np.transpose(V_Y_T)

Mprime = np.dot(np.transpose(Q_D), W_D)
Uprime, Sigmaprime, Vprime_T = linalg.svd(Mprime, full_matrices = False)
Vprime = np.transpose(Vprime_T)

Xprime = X
Yprime = Y

for i in range(COLS):
	sumOfCol = 0
	for j in range(ROWS):
		sumOfCol += (X[j][i] + Y[j][i])
	sumOfCol /= (ROWS + ROWS)
	for j in range(ROWS):
		Xprime[j][i] -= sumOfCol
		Yprime[j][i] -= sumOfCol

## Restore the diagonal matrices back to full size
Sigma_X = np.diag(Sigma_X)
# Sigma_X = np.concatenate((Sigma_X, np.zeros((ROWS - COLS, COLS))), axis = 0)
Sigma_Y = np.diag(Sigma_Y)
# Sigma_Y = np.concatenate((Sigma_Y, np.zeros((ROWS - COLS, COLS))), axis = 0)

Q_aligned = np.dot(np.dot(np.dot(Xprime, V_X), np.linalg.pinv(Sigma_X)), Uprime)
W_aligned = np.dot(np.dot(np.dot(Yprime, V_Y), np.linalg.pinv(Sigma_Y)), Vprime)



print(Q_aligned)
print(W_aligned)

