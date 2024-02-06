from math import log
def cross_entrop(y_hat, y_actual):
    # infinite error for confident wrong predictions
    loss = log(y_hat) if y_actual else log(1-y_hat)
    return -1*loss