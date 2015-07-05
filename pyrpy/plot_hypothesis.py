from math import sqrt
from pyrpy.plot_density import plot_density
from pyrpy.plot_distribution import plot_distribution
from pyrpy.mean import mean
from pyrpy.sd import sd
from matplotlib import pyplot as plt

def plot_hypothesis(x, conf=0.95):
    """
    Plots a density distribution of the actual data, along with a t distribution
    of the likely range of values for the mean given the sample size, with a
    shaded confidence interval.

    TODO: will allow for plotting the distribution of a comparison data sample
    so you can compare the two samples visually.


    :param x:
    :param conf:
    :return:
    """
    # TODO: Make the two plots actually overlay on top of each other.
    SE = sd(x) / sqrt(len(x))
    plot_distribution("t", df=len(x)-1, mean=mean(x), sd=SE, primary=False)
    plot_density(x, primary=False)
    plt.show()
