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

def mpl_span_columns(usetex=False):
    """
    Set matplotlib to make pretty plots for publishing figs that
    span 2-columns.
    """
    plt.rcdefaults()
    plt.rc('font', family='serif')
    plt.rc('figure', figsize=(7,5.5))
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    plt.rc('text', usetex=usetex)

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

def mpl_thumbnails(usetex=False):
    """
    Make png thumbnails
    """
    # XXX -- change the defaults above to pdf, remove .pdf from filename
