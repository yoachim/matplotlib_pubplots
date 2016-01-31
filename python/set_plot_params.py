import matplotlib.pylab as plt
import os

def plot_multi_format(plot_funcs, usetex=False, outdir='plots',
                      setting_funcs=None):
    """
    Outputs plots formatted 3 ways: Publication ready, PowerPoint ready, and png thumbnails.

    input
    -----
    plot_funcs : List of functions that return a mpl figure and a filename (or list of figures and filenames)

    """
    if setting_funcs is None:
        setting_funcs = {'single': mpl_single_column,
                         'slides': mpl_slides,
                         'thumbnails': mpl_thumbnails}

    if not os.path.exists(outdir):
        os.makedirs(outdir)
    # For python 3.4
    # os.makedirs(outdir, exist_ok=True)

    for key in setting_funcs.keys():
        setting_funcs[key](usetex=usetex)
        for plot_func in plot_funcs:
            figs, names = plot_func()
            for fig,name in zip(figs,names):
                fig.savefig(os.path.join(outdir, key+'_'+name))
            plt.close('all')

def mpl_single_column(usetex=False):
    """
    Set matplotlib to make pretty plots for publishing in 2-column
    """
    plt.rcdefaults()
    plt.rc('font', family='serif')
    plt.rc('figure', figsize=(4,3))
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    plt.rc('text', usetex=usetex)
    plt.rc('savefig', format='pdf', bbox='tight')

def mpl_slides(usetex=False):
    """
    Set matplotlibrc to make pretty slides
    """
    plt.rcdefaults()
    plt.rc('font', family='serif')
    # The default PowerPoint page setup
    plt.rc('figure', figsize=(7,5.5))
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
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
    plt.rc('figure', figsize=(3,3))
