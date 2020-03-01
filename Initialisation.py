from scipy.stats import norm
import numpy as np

RATE = 0


class Option:
    def __init__(self, strike: float, tte: float, vol: float, typ: str):
        assert typ in ['C', 'P']
        self.strike = strike
        self.tte = tte
        self.vol = vol
        self.typ = typ
        self.payoff_func = None
        self.price_func = None
        self.delta_func = None
        self.gamma_func = None
        self.vega_func = None
        self.theta_func = None

    def add_payoff_func(self):
        def func(x):
            if self.typ == 'C':
                return max(x - self.strike, 0)
            else:
                return max(self.strike - x, 0)
        self.payoff_func = func

    @staticmethod
    def get_greeks_and_price(strike: float, vol: float, rate: float, tte: float, typ: str):
        def d1(x):
            return (np.log(x / strike) + (rate + (vol ** 2) / 2) * tte) / (vol * tte)

        def d2(x):
            return d1(x) - vol * tte

        def price(x):
            return norm.cdf(d1(x)) * x - norm.cdf(d2(x)) * strike * np.exp(-rate * tte)

        def delta(x):
            return norm.cdf(d1(x)) if typ == 'C' else norm.cdf(d1(x)) - 1

        def gamma(x):
            return norm.pdf(d1(x)) / (x * vol * np.sqrt(tte))

        def vega(x):
            return x * norm.pdf(d1(x)) * np.sqrt(tte)

        def theta(x):
            theta_part_1 = - x * norm.pdf(d1(x)) * vol / (2 * np.sqrt(tte))
            if typ == 'C':
                theta_both_parts = theta_part_1 - rate * strike * np.exp(-rate * tte) * norm.cdf(d2(x))
            else:
                theta_both_parts = theta_part_1 + rate * strike * np.exp(-rate * tte) * norm.cdf(-d2(x))
            return theta_both_parts

        return price, delta, gamma, vega, theta

    def add_greeks_and_price(self):
        self.price_func, self.delta_func, self.gamma_func, self.vega_func, self.theta_func = Option.get_greeks_and_price(
            self.strike, self.vol, RATE, self.tte, self.typ)


def create_option(strike: float, tte: float, vol: float, typ: str) -> Option:
    option = Option(strike, tte, vol, typ)
    option.add_payoff_func()
    option.add_greeks_and_price()
    return option
