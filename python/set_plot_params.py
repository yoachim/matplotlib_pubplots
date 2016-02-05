import matplotlib.pylab as plt
import os

def plot_multi_format(plot_funcs, plot_kwargs=None,
                      usetex=False, outdir='plots',
                      setting_funcs=['single', 'span', 'slides', 'thumbnails']):
    """
    Outputs plots formatted 3 ways: Publication ready, PowerPoint ready, and png thumbnails.

    input
    -----
    plot_funcs : List of functions that return a mpl figure and a filename (or list of figures and filenames)

    """

    setting_dict = {'single': mpl_single_column,
                    'span': mpl_span_columns,
                    'slides': mpl_slides,
                    'thumbnails': mpl_thumbnails}

    if not os.path.exists(outdir):
        os.makedirs(outdir)
    # For python 3.4
    # os.makedirs(outdir, exist_ok=True)

    if plot_kwargs is None:
        plot_kwargs=[{}]*len(plot_funcs)

    for key in setting_funcs:
        setting_dict[key](usetex=usetex)
        for plot_func,pkwargs in zip(plot_funcs,plot_kwargs):
            figs, names = plot_func(**pkwargs)
            for fig,name in zip(figs,names):
                fig.savefig(os.path.join(outdir, key+'_'+name))
            plt.close('all')

def mpl_single_column(usetex=False):
    """
    Set matplotlib to make pretty plots for publishing in 2-column
    """
    plt.rcdefaults()
    plt.rc('font', family='serif', size=12.0, style='normal')
    plt.rc('figure', figsize=(4,3))
    plt.rc('axes', titlesize=12, labelsize=10)
    plt.rc('legend', fontsize=8, numpoints=1, scatterpoints=1)
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    plt.rc('text', usetex=usetex)
    plt.rc('savefig', format='pdf', bbox='tight')


def mpl_span_columns(usetex=False):
    """
    Set matplotlib to make pretty plots for publishing a full-page figure
    """
    plt.rcdefaults()
    plt.rc('font', family='serif', size=12.0, style='normal')
    plt.rc('figure', figsize=(7, 5.25))
    plt.rc('axes', titlesize=12, labelsize=10)
    plt.rc('legend', fontsize=8, numpoints=1, scatterpoints=1)
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    plt.rc('text', usetex=usetex)
    plt.rc('savefig', format='pdf', bbox='tight')


def mpl_slides(usetex=False):
    """
    Set matplotlibrc to make pretty slides
    """
    plt.rcdefaults()
    plt.rc('font', family='serif', size=18)
    # The default PowerPoint page setup
    plt.rc('figure', figsize=(7,5.5))
    plt.rc('axes', titlesize=24, labelsize=16, linewidth=3)
    plt.rc('legend', fontsize=18, numpoints=1, scatterpoints=1)
    plt.rc('xtick', labelsize='small')
    plt.rc('ytick', labelsize='small')
    plt.rc('text', usetex=usetex)
    plt.rc('lines', linewidth=5)
    plt.rc('savefig', format='pdf', bbox='tight')

def mpl_thumbnails(usetex=False):
    """
    Make png thumbnails
    """
    plt.rcdefaults()
    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    plt.rc('text', usetex=usetex)
    plt.rc('savefig', format='pdf', bbox='tight')
    plt.rc('savefig', format='png', bbox='tight')
    plt.rc('figure', figsize=(4,3))
