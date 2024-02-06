import random
# Split Martingale (Labouchere system) is a betting strategy for roulette
def split_martingale(seq, balance):
    # win game return balance and profits
    if len(seq) < 1:
        return balance
    
    # if sequence is of length 1, the bet is the remaining number in the sequence
    # Else, first number in list
    if len(seq) == 1:
        bet = seq[0]
    else:
        bet = seq[0] + seq[-1]
    
    # lost game, cant bet again
    if bet > balance:
        return balance
    
    won = random.randint(0,37)
    
    # if betting on color then "win" if less than 18
    # let 0-17 (inclusive) be red, 18-35 (inclusive) black, 36 and 37 green
    if won < 18:
        return split_martingale(seq[1:-1], balance + bet)
    else:
        return split_martingale(seq + [bet], balance - bet)


#test code
for i in range(0,10):
    print(split_martingale([10,20,40,20,10], 1000))