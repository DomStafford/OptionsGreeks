import matplotlib.pyplot as plt
from Initialisation import create_option


def plot_greeks(option, x_range: tuple = (0, 100), step: float = 0.01):
    x_data = [i * step for i in range(x_range[0], int(x_range[1] / step))]
    payoff_data = [option.payoff_func(x) for x in x_data]
    price_data = [option.price_func(x) for x in x_data]
    delta_data = [option.delta_func(x) for x in x_data]
    gamma_data = [option.gamma_func(x) for x in x_data]
    theta_data = [option.theta_func(x) for x in x_data]
    vega_data = [option.vega_func(x) for x in x_data]

    fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, 1, figsize=(10, 15))
    for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
        ax.set(xlim=x_range)
        ax.hlines(0, x_range[0], x_range[1])
    ax1.plot(x_data, payoff_data, c='black')
    ax2.plot(x_data, price_data, c='orange')
    ax3.plot(x_data, delta_data, c='blue')
    ax4.plot(x_data, gamma_data, c='green')
    ax5.plot(x_data, theta_data, c='red')
    ax6.plot(x_data, vega_data, c='yellow')

    ax6.set_xlabel('Spot')
    ax1.set_ylabel('Intrinsic value')
    ax2.set_ylabel('Price')
    ax3.set_ylabel('Delta')
    ax4.set_ylabel('Gamma')
    ax5.set_ylabel('Theta')
    ax6.set_ylabel('Vega')
    plt.show()


def plot_greeks_spot_fixed(spot: float, tte: float, vol: float, strike_range: tuple = (0, 100), step: float = 0.01):
    x_data = [i * step for i in range(strike_range[0], int(strike_range[1] / step))]
    calls = [create_option(strike=x, tte=tte, vol=vol, typ='C') for x in x_data]
    delta_data = [call.delta_func(spot) for call in calls]
    gamma_data = [call.gamma_func(spot) for call in calls]
    theta_data = [call.theta_func(spot) for call in calls]
    vega_data = [call.vega_func(spot) for call in calls]

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10, 10))

    for ax in [ax1, ax2, ax3, ax4]:
        ax.set(xlim=strike_range)
        ax.hlines(0, strike_range[0], strike_range[1])

    ax1.plot(x_data, delta_data, c='blue')
    ax2.plot(x_data, gamma_data, c='green')
    ax3.plot(x_data, theta_data, c='red')
    ax4.plot(x_data, vega_data, c='yellow')

    ax4.set_xlabel('Strike')
    ax1.set_ylabel('Delta')
    ax2.set_ylabel('Gamma')
    ax3.set_ylabel('Theta')
    ax4.set_ylabel('Vega')
    plt.show()
