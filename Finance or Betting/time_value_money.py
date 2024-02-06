import math as math
class TVM():
    def __init__(self):
         super().__init__()

    def EAR(self, r, n):
        """ Effective Annual Rate
        Parameters
        ----------
        r : float
            Standard interest rate
        n : int
            Number of interest payments per year
        """
        return ((1 + (r / n)) ** n) - 1

    def fv_single(self, r, pv, n):
        """ Future Value of a single cash flow
        Parameters
        ----------
        r : float
            Interest rate per period
        pv : float
            Present value of investment
        n : int
            Number of interest payments per period
        """
        return pv * ((1 + r) ** n)

    def pv_single(self, r, fvn, n):
        """ Present Value of a single cash flow
        Parameters
        ----------
        r : float
            Interest rate per period
        fvn : float
            Future value of investment after n periods
        n : int
            Nnumber of interest payments per period
        """
        return fvn / ((1 + r) ** n)

    def fv_multi(self, r, pv, n, m):
        """ Future Value of investment pay more than once per year
        Parameters
        ----------
        r : float
            Stated annual interest rate per period
        pv : float
            Present value of investment
        n : int
            Number of years
        m : int
            Number of compounding periods per year
        """
        return pv * ((1 + r) ** (m * n))

    def pv_multi(self, r, fvn, n, m):
        """ Present Value of investment pay more than once per year
        Parameters
        ----------
        r : float
            Stated annual interest rate per period
        fv : float
            Future value of investment after n periods
        n : int
            Number of years
        m : int
            Number of compounding periods per year
        """
        return fvn / ((1 + r) ** (m * n))

    def fv_cont_comp(self, r, pv, n):
        """ Future Value of investment with continuous compounding
        Parameters
        ----------
        r : float
            Stated annual interest rate per period
        pv : float
            Present value of investment
        n : int
            The number of years 
        """
        return pv * (math.e ** (r * n))

    def fv_ord_annuity(self, A, r, n):
        """ Future Value of ordinary annuity after n periods
        Parameters
        ----------
        A : float
            Annuity amount
        r : float
            Interest rate per period
        n : int
            Number of periods
        """
        return A * ((((1 + r) ** n) - 1) / r)

    def pv_ord_annuity(self, A, r, n):
        """ Present Value of ordinary annuity
        Parameters
        ----------
        A : float
            Annuity amount
        r : float
            Interest rate per period
        n : int
            Number of periods
        """
        return A * ((1 - (1 / ((1 + r) ** n))) / r)

    def fv_annuity_due(self, A, r, n):
        """ Future Value of annuity due
        Parameters
        ----------
        A : float
            Annuity amount
        r : float
            Interest rate per period
        n : int
            Number of periods
        """
        return self.fv_ord_annuity(A, r, n) * (1 + r)

    def pv_annuity_due(self, A, r, n):
        """ Present Value of annuity due
        Parameters
        ----------
        A : float
            Annuity amount
        r : float
            Interest rate per period
        n : int
            Number of periods
        """
        return self.pv_ord_annuity(A, r, n) * (1 + r)

    def pv_perp(self, A, r):
        """ Present value of a Perpetuity
        Parameters
        ----------
        A : float
            Annuity amount
        r : float
            Interest rate
        """
        return (A / r)

    def fv_uneq_cf(self, cf_series, r, n):
        """ Future Value of a series of unequal cash flows
        Parameters
        ----------
        cf_series : list
            List of series of cashflows
        r : float
            Interest rate
        n : int
            Number of cash flows
        """
        return sum(cf_series[i] * ((1 + r) ** (i + 1)) for i in range(0,n))

    def net_pv(self, cf_series, r, n):
        """ Net Present Value
        Parameters
        ----------
        cf_series : list
            List of expected cashflow at time t(index)
        r : float
            Discount rate or opportunity cost
        n : int
            Investment projected life
        """
        return sum((cf_series[t] / ((1 + r) ** t)) for t in range(0,n))
        
    def HPR_no_cf(self, end, beg):
        """ Holding Period Return no Cashflows
        Parameters
        ----------
        end : float
            Ending value
        beg : float
            Begining value
        """
        return ((end - beg) / beg)

    def HPR(self, end, beg, dividend):
        """ Holding Period Return with Cashflows
        Parameters
        ----------
        end : float
            Ending value
        beg : float
            Begining value
        dividend : float
            The dividend recieved
        """
        return ((end - beg + dividend) / beg)

    def BDY(self, D, F, t):
        """ Yield on a Bank Discount Basis
        Parameters
        ----------
        D : float
            Dollar discount, equal to the difference between face value of
            bill and purchase price
        F : float
            Face value of t-bill
        t : int
            Days remaining until maturity
        """
        return ((D / F) * (360 / t))

    def EAY(self, end, beg, dividend, t):
        """ Effective Annual Yield
        Parameters
        ----------
        end : float
            Ending Value
        beg : float
            Begining Value
        dividend : float
            The dividend recieved
        t : int
            Days remaining until maturity
        """
        return (((1 + self.HPR(end, beg, dividend)) ** (360 / t)) - 1)

    def money_market_yield(self, t, r):
        """ Money Market Yield
        Parameters
        ----------
        t : float
            Days remaining until maturity
        r : float
            Bond discount rate
        """
        return ((360 * r) * (360 - (t * r)))