from matplotlib import pyplot as plt

def plot(x, y):
    """
    plots
    :param x: (array like)
        the data
    """


    plt.plot(x,y, color='#0066FF', alpha=0.7)

    # Add Grid lines
    plt.minorticks_on()
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    # Render the plot
    plt.show()

