import numpy as np
from scipy import linalg
def least_squares(A, b_bar):
    # formats the matrix A
    A = np.hstack((np.ones((A.size, 1)), np.reshape(A, (A.size, 1))))
    # formats matrix b_bar
    b_bar = np.reshape(b_bar, (b_bar.size, 1))
    
    # matrix of the transpose of A
    AT = A.transpose()
    # matrix multiplication of AT and A (2x2 matrix)
    AT_A = AT @ A
    # matrix multiplication of AT and b_bar (2x1 matrix)
    AT_b = AT @ b_bar

    # solution to the linear system (b + mx = y)
    M_sol = np.linalg.solve(AT_A, AT_b)
    return M_sol

# your x and y values here
x = np.array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9])
y = np.array([10, 20, 25, 30, 40, 45, 40, 50, 60, 55])

mb_sol = least_squares(x, y)
m = float(mb_sol[1])
b = float(mb_sol[0])

print('The best fit for m: {slope:.3f}'.format(slope = m))
print('The best fit for b: {intercept:.3f}'.format(intercept = b))
print('The equation of the line is y = {slope:.3f}x + {intercept:.3f}'.format(slope = m, intercept = b))