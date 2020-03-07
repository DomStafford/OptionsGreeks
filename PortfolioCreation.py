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

    def add_function_attribute(self, attr: str):
        def func(x):
            result = 0
            for option in self.lst:
                result += getattr(option[0], attr + '_func')(x) * option[1]
            return result
        setattr(self, attr + '_func', func)

    def add_greek_funcs(self):
        for attr in ['payoff', 'price', 'delta', 'gamma', 'theta', 'vega', 'rho', 'volga', 'charm', 'vanna']:
            self.add_function_attribute(attr)


def create_call_fly(strikes: List[float], tte: float, vol: float) -> Portfolio:
    assert strikes[0] < strikes[1] < strikes[2]
    call_fly = Portfolio()
    call_fly.add_option(strike=strikes[0], tte=tte, vol=vol, typ='C', volume=1)
    call_fly.add_option(strike=strikes[1], tte=tte, vol=vol, typ='C', volume=-2)
    call_fly.add_option(strike=strikes[2], tte=tte, vol=vol, typ='C', volume=1)
    call_fly.add_greek_funcs()
    return call_fly


def create_call_calendar(strike: float, tte_1: float, tte_2: float, vol: float) -> Portfolio:
    assert tte_1 < tte_2
    calendar = Portfolio()
    calendar.add_option(strike=strike, tte=tte_1, vol=vol, typ='C', volume=-1)
    calendar.add_option(strike=strike, tte=tte_2, vol=vol, typ='C', volume=1)
    calendar.add_greek_funcs()
    return calendar

