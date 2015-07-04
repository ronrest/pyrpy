import matplotlib.pyplot as plt

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
    # TODO: add an extra element at the cutoff points to avoid sloping effect.
    y2 = [0 if ((x[i] > lower) and (x[i] < upper))
        else y[i]
        for i in range(len(x))]

    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(main)
    plt.fill_between(x, y, y2, facecolor='blue', alpha=0.5)
    plt.show()
