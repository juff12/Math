import math as math
# returns the square root of a function using newton method
# equation of the form f(x) = x^2 - num
# num: the number to find sqrt of
# x0: initial guess
# accuracy: value the result is within (error) 
# max_itr: max number of trials
def newton_method(num, x0, accuracy, max_itr):
    def function(x, num):
        # f(x) of square root problem
        return (x ** 2) - num 
    def derivative(x):
        # returns the derivative of f(x)
        return 2 * x
    x1 = 1 - (function(1, num) / derivative(1)) # formula of newton method
    # breaks when the difference between x1 and x0 is accurate to three decimal places
    for i in range(0, max_itr):
        x0 = x1
        x1 = x1 - (function(x1, num) / derivative(x1))
        if abs(x1 - x0) <= accuracy:
            return x1
    return None # failed to find solution

# Tests

x_1 = 16
x_2 = 14
x_3 = 1
x_4 = 0

#checks that the solution is within 0.001 of correct value
def AlmostEqual(P, Q, digits):
    epsilon = 10 ** -digits
    return (P-Q) < epsilon

assert AlmostEqual(4,newton_method(x_1, 0, 0.001, 1000), 3)
assert AlmostEqual(3.7416,newton_method(x_2, 0, 0.001, 1000), 3)
assert AlmostEqual(1, newton_method(x_3, 0, 0.001, 1000), 3)
assert AlmostEqual(0, newton_method(x_4, 0, 0.001, 1000), 3)


#comments: possible additions -> add maximum number of itterations, allow user to pick epsilon value