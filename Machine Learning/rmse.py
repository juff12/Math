# calculate the Mean Square Error
# data: array of tuples of x,y values [(x0,y0),(x1,y1)]
# m: slope
# b: y intercept
def rmse(data, m, b):
    n = len(data)
    sq_err = 0
    for x, y in data:
        # find predicted y
        y_hat = m*x + b
        # squared difference between predicted and actual value
        sq_err += (y - y_hat) ** 2
    #average squared differance
    mean_sq_err = sq_err / n
    # sqrt for original units
    return mean_sq_err ** .5