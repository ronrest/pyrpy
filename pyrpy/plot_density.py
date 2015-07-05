from matplotlib import pyplot as plt
from numpy import linspace
from scipy.stats import gaussian_kde

def plot_density(x, primary=True):
    """
    Creates a density plot of the data.

    Code is based on this forum message http://stackoverflow.com/a/4152016

    :param x: (array like)
        the data
    """

    # Calculate the density points
    density = gaussian_kde(x)
    # TODO: COme up with a better start and end point
    xs = linspace(min(x)-1, max(x)+1, 200)
    density.covariance_factor = lambda : 0.25
    density._compute_covariance()
    plt.plot(xs,density(xs), color='#0066FF', alpha=0.7)

    # Add Grid lines
    plt.minorticks_on()
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    # Render the plot
    if primary:
        plt.show()

