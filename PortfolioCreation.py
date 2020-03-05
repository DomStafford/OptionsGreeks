from Initialisation import create_option
from typing import List


class Portfolio:
    def __init__(self):
        self.lst = []
        self.payoff_func = None
        self.price_func = None
        self.delta_func = None
        self.gamma_func = None
        self.theta_func = None
        self.vega_func = None
        self.rho_func = None
        self.volga_func = None
        self.charm_func = None
        self.vanna_func = None

    def add_option(self, strike: float, tte: float, vol: float, typ: str, volume: int, rate: float = 0):
        self.lst.append([create_option(strike, tte, vol, typ, rate), volume])

    def add_payoff_func(self):
        def func(x):
            result = 0
            for option in self.lst:
                result += option[0].payoff_func(x) * option[1]
            return result
        self.payoff_func = func

    def add_price(self):
        def func(x):
            result = 0
            for option in self.lst:
                result += option[0].price_func(x) * option[1]
            return result
        self.price_func = func

    def add_greek_funcs(self):
        def delta(x):
            result = 0
            for option in self.lst:
                result += option[0].delta_func(x) * option[1]
            return result

        def gamma(x):
            result = 0
            for option in self.lst:
                result += option[0].gamma_func(x) * option[1]
            return result

        def theta(x):
            result = 0
            for option in self.lst:
                result += option[0].theta_func(x) * option[1]
            return result

        def vega(x):
            result = 0
            for option in self.lst:
                result += option[0].vega_func(x) * option[1]
            return result

        def rho(x):
            result = 0
            for option in self.lst:
                result += option[0].rho_func(x) * option[1]
            return result

        def charm(x):
            result = 0
            for option in self.lst:
                result += option[0].charm_func(x) * option[1]
            return result

        def volga(x):
            result = 0
            for option in self.lst:
                result += option[0].volga_func(x) * option[1]
            return result

        def vanna(x):
            result = 0
            for option in self.lst:
                result += option[0].vanna_func(x) * option[1]
            return result

        self.delta_func = delta
        self.gamma_func = gamma
        self.theta_func = theta
        self.vega_func = vega
        self.rho_func = rho
        self.charm_func = charm
        self.volga_func = volga
        self.vanna_func = vanna

    def add_everything(self):
        self.add_payoff_func()
        self.add_greek_funcs()
        self.add_price()


def create_call_fly(strikes: List[float], tte: float, vol: float) -> Portfolio:
    assert strikes[0] < strikes[1] < strikes[2]
    call_fly = Portfolio()
    call_fly.add_option(strike=strikes[0], tte=tte, vol=vol, typ='C', volume=1)
    call_fly.add_option(strike=strikes[1], tte=tte, vol=vol, typ='C', volume=-2)
    call_fly.add_option(strike=strikes[2], tte=tte, vol=vol, typ='C', volume=1)
    call_fly.add_everything()
    return call_fly


def create_call_calendar(strike: float, tte_1: float, tte_2: float, vol: float) -> Portfolio:
    assert tte_1 < tte_2
    calendar = Portfolio()
    calendar.add_option(strike=strike, tte=tte_1, vol=vol, typ='C', volume=-1)
    calendar.add_option(strike=strike, tte=tte_2, vol=vol, typ='C', volume=1)
    calendar.add_everything()
    return calendar

