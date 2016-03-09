import matplotlib.pylab as plt
import numpy as np
from set_plot_params import plot_multi_format


def example_plot1():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x = np.linspace(1., 8., 30)
    ax.set_title('Title!')
    ax.plot(x, x ** 1.5, color='k', ls='solid', label='line 1')
    ax.plot(x, 20/x, color='0.50', ls='dashed', label='line 2')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (K)')
    ax.legend(loc='upper left')
    fig.tight_layout()
    return [fig], ['example_1']

# Should make an OO example where __init__ sets up data, then methods plot it different ways. Should be able to just pass methods along...



if __name__ == '__main__':

    fig_funcs = [example_plot1]
    plot_multi_format(fig_funcs)
