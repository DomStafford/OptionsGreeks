import matplotlib.pyplot as plt
from Initialisation import create_option

COLOURS =['red', 'green', 'magenta', 'violet', 'chocolate', 'crimson',
               'darkorchid', 'lime', 'lavender', 'mistyrose']


def plot_greeks(option, x_range: tuple = (0, 100), step: float = 0.1):
    global COLOURS
    x_data = [i * step for i in range(x_range[0], int(x_range[1] / step))]
    attrs = ['payoff', 'price', 'delta', 'gamma', 'theta', 'vega', 'rho', 'charm', 'volga', 'vanna']
    dic = {}
    for attr in attrs:
        dic[attr] = [getattr(option, attr + '_func')(x) for x in x_data]
    fig, axes = plt.subplots(10, 1, figsize=(10, 35))
    for ax, attr, col in zip(axes, attrs, COLOURS):
        ax.set(xlim=x_range)
        ax.hlines(0, x_range[0], x_range[1])
        ax.plot(x_data, dic[attr], c=col)
        ax.set_xlabel('Spot')
        ax.set_ylabel(attr.capitalize())
    plt.show()


def plot_greeks_spot_fixed(spot: float, tte: float, vol: float, strike_range: tuple = (0, 100), step: float = 0.01):
    global COLOURS
    x_data = [i * step for i in range(strike_range[0], int(strike_range[1] / step))]
    calls = [create_option(strike=x, tte=tte, vol=vol, typ='C') for x in x_data]
    puts = [create_option(strike=x, tte=tte, vol=vol, typ='P') for x in x_data]
    attrs = ['payoff', 'gamma', 'theta', 'vega', 'charm', 'volga', 'vanna']
    attrs_for_both = ['delta', 'rho', 'price']
    dic = {}
    for attr in attrs:
        dic['call_' + attr] = [getattr(call, attr + '_func')(spot) for call in calls]
    for attr in attrs_for_both:
        dic['call_' + attr] = [getattr(call, attr + '_func')(spot) for call in calls]
        dic['put_' + attr] = [getattr(put, attr + '_func')(spot) for put in puts]
    fig, axes = plt.subplots(len(attrs + attrs_for_both), 1, figsize=(10, 30))
    attrs_in_order = ['payoff', 'price', 'delta', 'gamma', 'theta', 'vega', 'rho', 'charm', 'volga', 'vanna']
    for ax, attr, col in zip(axes, attrs_in_order, COLOURS):
        if attr in attrs_for_both:
            ax.set(xlim=strike_range)
            ax.plot(x_data, dic['call_' + attr], c=col, label='Call')
            ax.plot(x_data, dic['put_' + attr], label='Put')
            ax.set_xlabel('Strike')
            ax.set_ylabel(attr.capitalize())
            ax.legend()
        else:
            ax.set(xlim=strike_range)
            ax.plot(x_data, dic['call_' + attr], c=col)
            ax.set_xlabel('Strike')
            ax.set_ylabel(attr.capitalize())
    plt.show()
