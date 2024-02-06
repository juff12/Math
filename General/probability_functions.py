import math as math
import numpy as np
import pandas as pd

class Probability():
    def __init__(self):
         super().__init__()

    # odds of event 
    # p: probability of event
    def odds_for_event(self, p):
        """ Odds of event
        Parameters
        ----------
        p : float
            probability of event            
        
        Returns
        -------
        float
            a float of the probability of event
        """
        return (p / (1 - p))

    def cond_prob(self, pA, pB):
        """ Conitional probability of event A|B given that A and B are independent
        Parameters
        ----------
        pA : float
            probability of event A            
        pB : float
            probability of event B
        
        Returns
        -------
        float
            a float of the probability of event A|B
        """
        return ((pA * pB) / pB)

    # combination formula for combinatorics
    # n: total objects
    # r: selected objects
    def combination(self, n, k):
        """ Combination formula
        Parameters
        ----------
        n : int
            total objects
        k : int
            selected objects
        
        Returns
        -------
        int
            a int of total number of choices
        """
        return (math.factorial(n) / (math.factorial(n - k) * math.factorial(k)))

    # permutation formula for permutations
    # n: total objects
    # r: selected objects
    def permutation(self, n, k):
        """ Permutation formula
        Parameters
        ----------
        n : int
            total objects
        k : int
            selected objects
        
        Returns
        -------
        int
            a int of total number of choices
        """
        return (math.factorial(n) / math.factorial(n - k))

    def binomial_prob(self, n, k, p):
        """ Binomial Probability Function
        Parameters
        ----------
        n : int
            number of trials
        k : int
            selected objects
        p : float
            probability of object
        
        Returns
        -------
        float
            a float of the binonmial probability of an event
        """
        return ((self.combination(n, k) * p) * ((1 - p) ** (n - k)))

    # Table of Marginal Distribution for variable X
    # n: number of possible values of X
    # p: probability of X being true
    def marginal_dist(self, n, p):
        """ Table of Marginal Distribution for variable X
        Parameters
        ----------
        n : int
            number of possible values to choose from
        p : float
            probability that choice x is chosen
        
        Returns
        -------
        DataFrame
            a DataFrame of the pobabilities of X
        """
        # function to find probability of each marginal value
        func = lambda x, y, p: self.combination(x, y) * (p ** y) * ((1 - p) ** (x - y))
        # array of data
        data = np.asarray([func(n, k, p) for k in range(0,n+1)])
        index_labels = np.asarray(["X=" + str(i) for i in range(0,n+1)])
        df = pd.DataFrame(data, index=index_labels, columns=["P(X)"])
        return df


    def joint_dist(self, n, px, py):
        """ Table of Joint Distribution of X and Y
        Parameters
        ----------
        n : int
            number of possible values to choose from
        px : float
            probability that choice x is chosen
        py : float
            probability that choice y is chosen
            
        Returns
        -------
        DataFrame
            a DataFrame of the pobabilities of X and Y
        """
        # function to find the number of combinations of the partition
        part_func = lambda n, x, y: (math.factorial(n)
                                / (math.factorial(x) * math.factorial(y) * math.factorial(n-x-y)))
        # the probability of event (x,y) where x is the number of x and y is number of y objects
        prob_func = lambda n, x, y, px, py: (part_func(n,x,y) 
                                            * (px ** x) 
                                            * (py ** y) 
                                            * ((1-px-py) ** (n-x-y)))
        # checks that the (x,y) pair is valid, invalid if x+y > n
        valid_func = lambda n, x, y, px, py: prob_func(n,x,y,px,py) if (n-x-y >= 0) else 0
        # array of data
        data = np.asarray([[valid_func(n, x, y, px, py) for x in range(0,n+1)] for y in range(0,n+1)])
        row_labels = np.asarray(["Y=" + str(i) for i in range(0,n+1)]) # labels for rows
        col_labels = np.asarray(["X=" + str(i) for i in range(0,n+1)]) # labels for col
        df = pd.DataFrame(data.reshape((n+1,n+1)), index=row_labels, columns=col_labels)
        return df
