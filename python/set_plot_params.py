import matplotlib as plt


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
    plt.rc('figure', figsize=(4,3))
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    plt.rc('text', usetex=usetex)
    plt.rc('savefig', format='pdf', bbox='tight')
    plt.rc('savefig', format='png', bbox='tight')
