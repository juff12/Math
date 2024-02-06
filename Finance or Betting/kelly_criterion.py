# kelly criterion determines the amount to bet based on:
# p: probability to win
# q: probability to lose
# b: proportion of bet gained with a win
def kelly_criterion_bet(p, q, b):
    return p - (q / b)


# kelly criterion determines the amount to invest based on:
# p: the probability the investment increases in value
# q: the probability the investment decreases in value
# a: the fraction that is lost in a negative outcome (price falls 10%, a = 0.01)
# b: the fraction that is gained in a positive outcome (price increases 10%, b = 0.01)
def kelly_criterion(p, q, a, b):
    # win-loss probability ratio, ratio of winning to losing bets
    WLP = p / (1-p)
    # win-loss ratio of bet outcomes, winning skew
    WLR = b / a
    return (p / a) * (1 - (1 / WLP) * (1 / WLR))

