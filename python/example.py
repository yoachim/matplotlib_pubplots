import matplotlib.pylab as plt
import numpy as np
from set_plot_params import mpl_single_column, mpl_span_columns,mpl_slides


def example_plot1():
    fig = plt.figure(figsize=(4, 3))
    ax = fig.add_subplot(1, 1, 1)
    x = np.linspace(1., 8., 30)
    ax.plot(x, x ** 1.5, color='k', ls='solid')
    ax.plot(x, 20/x, color='0.50', ls='dashed')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (K)')
    fig.tight_layout()
    return [fig], ['example_1.pdf']


if __name__ == '__main__':

    setting_funcs = {'single':mpl_single_column,
                     'span':mpl_span_columns, 'slides':mpl_slides}
    fig_funcs = [example_plot1]


    # I could turn this loop into a function.

    for key in setting_funcs.keys():
        setting_funcs[key]()
        for fig_func in fig_funcs:
            figs, names = fig_func()
            for fig,name in zip(figs,names):
                fig.savefig(key+name)
            plt.close('all')
