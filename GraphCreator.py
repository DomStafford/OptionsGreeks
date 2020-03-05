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
    rho_data = [option.rho_func(x) for x in x_data]
    charm_data = [option.charm_func(x) for x in x_data]
    volga_data = [option.volga_func(x) for x in x_data]
    vanna_data = [option.vanna_func(x) for x in x_data]

    fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10) = plt.subplots(10, 1, figsize=(10, 35))
    for ax in [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10]:
        ax.set(xlim=x_range)
        ax.hlines(0, x_range[0], x_range[1])
    ax1.plot(x_data, payoff_data, c='black')
    ax2.plot(x_data, price_data, c='orange')
    ax3.plot(x_data, delta_data, c='blue')
    ax4.plot(x_data, gamma_data, c='green')
    ax5.plot(x_data, theta_data, c='red')
    ax6.plot(x_data, vega_data, c='yellow')
    ax7.plot(x_data, rho_data, c='cyan')
    ax8.plot(x_data, volga_data, c='lime')
    ax9.plot(x_data, charm_data, c='magenta')
    ax10.plot(x_data, vanna_data, c='blueviolet')

    ax7.set_xlabel('Spot')
    ax1.set_ylabel('Intrinsic value')
    ax2.set_ylabel('Price')
    ax3.set_ylabel('Delta')
    ax4.set_ylabel('Gamma')
    ax5.set_ylabel('Theta')
    ax6.set_ylabel('Vega')
    ax7.set_ylabel('Rho')
    ax8.set_ylabel('Volga')
    ax9.set_ylabel('Charm')
    ax10.set_ylabel('Vanna')
    plt.show()


def plot_greeks_spot_fixed(spot: float, tte: float, vol: float, strike_range: tuple = (0, 100), step: float = 0.01):
    x_data = [i * step for i in range(strike_range[0], int(strike_range[1] / step))]
    calls = [create_option(strike=x, tte=tte, vol=vol, typ='C') for x in x_data]
    puts = [create_option(strike=x, tte=tte, vol=vol, typ='P') for x in x_data]
    delta_data = [call.delta_func(spot) for call in calls]
    put_delta_data = [put.delta_func(spot) for put in puts]
    gamma_data = [call.gamma_func(spot) for call in calls]
    theta_data = [call.theta_func(spot) for call in calls]
    vega_data = [call.vega_func(spot) for call in calls]
    rho_data = [call.rho_func(spot) for call in calls]
    put_rho_data = [put.rho_func(spot) for put in puts]
    call_price_data = [call.price_func(spot) for call in calls]
    put_price_data = [put.price_func(spot) for put in puts]

    fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, 1, figsize=(10, 30))

    for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
        ax.set(xlim=strike_range)
        ax.hlines(0, strike_range[0], strike_range[1])

    ax1.plot(x_data, delta_data, c='blue', label='Call')
    ax2.plot(x_data, gamma_data, c='green')
    ax3.plot(x_data, theta_data, c='red')
    ax4.plot(x_data, vega_data, c='yellow')
    ax5.plot(x_data, rho_data, c='cyan', label='Call')
    ax1.plot(x_data, put_delta_data, c='red', label='Put')
    ax5.plot(x_data, put_rho_data, c='green', label='Put')
    ax6.plot(x_data, call_price_data, c='orange', label='Call')
    ax7 = ax6.twinx()
    ax7.plot(x_data, put_price_data, c='red', label='Put')
    ax1.legend()
    ax5.legend()
    ax6.legend()

    ax5.set_xlabel('Strike')
    ax1.set_ylabel('Delta')
    ax2.set_ylabel('Gamma')
    ax3.set_ylabel('Theta')
    ax4.set_ylabel('Vega')
    ax5.set_ylabel('Rho')
    ax6.set_ylabel('Call price')
    ax7.set_ylabel('Put price')
    plt.show()
