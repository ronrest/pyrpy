import matplotlib.pyplot as plt
from numpy import concatenate

def shade_between(x, y, lower, upper, primary=None, type="l",
                  shade_col="blue", main="", xlab="", ylab=""):
    """
    Plots a graph, with a shaded region

    :param x:
    :param y:
    :param lower:
    :param upper:
    :param primary:
    :param type:
    :param shade_col:
    :param main:
    :param xlab:
    :param ylab:
    :return:
    """
    #---------------------------------------------------------------------------
    #                                                    Deal with Cutoff Points
    # ---------------------------------------------------------------------------
    # Splits the array up, so we can add duplicates of the cutoff points on the
    # x, otherwise we end up with lines that go up diagonally instead of
    # straight up
    below = [e for e in x if e <= lower]
    above = [e for e in x if e >= upper]
    i1 = len(below)
    i2 = len(x) - len(above)

    newx = concatenate([x[0:i1], [x[i1]], x[i1:i2], [x[i2]], x[i2:]])
    newy = concatenate([y[0:i1], [y[i1]], y[i1:i2], [y[i2]], y[i2:]])
    newy2 = concatenate([y[0:i1], [y[i1]], [0] * (i2 - i1), [0], y[i2:]])

    # Generate the plot
    plt.fill_between(newx, newy, newy2, color='#0066FF', alpha=0.7)

    # Add Labels
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(main)

    # Add Grid lines
    plt.minorticks_on()
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    # Display
    plt.show()
