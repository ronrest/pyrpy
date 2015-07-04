"""====================================================
                    DESCRIPTION

=======================================================
"""
__author__ = 'Ronny Restrepo'
from pyrpy.distributions import *
import matplotlib.pyplot as plt

# TODO: Create another function to show a normal curve/t curve of two samples
#       on top of each other, along with confidence intervals, just so we can
#       visually see the hypothesis test in action. If the null hypothesis was
#       rejected, then we can see by how much of a difference there is.



def plot_distribution(dist="normal", mean=None, sd=None, n=None, p=None, 
                      df=None, df2=None, rate=None, res=100, returndf=False, 
                      primary=True, plower=0.0001, pupper=0.9999):
    """
    ===========================================================================
                                                             PLOT DISTRIBUTION
    ===========================================================================
    Plots what a particular distribution looks like given parameters such as
    its mean and standard deviation.

    ARGS:
      dist    : "normal" "poisson" "binomial" "t" "f" "exp" determines the
                distribution to use.
      mean    : numeric. The mean of the distribution. If using poisson, this
                is ths lambda value.
                DEFAULT = 0 if using normal distribution.
                DEFAULT = 1 if using poisson distribution.
      sd      : Standard deviation.
                DEFAULT = 1
      n       : int. Used when dealing with binomial distribution. The number
                of times we run the binomial event, eg flip a coin.
                DEFAULT: 1
      p       : numeric. probability of success when using binomial
                deistribution
                DEFAULT: 0.5
      df      : Degrees of Freedom when using t distribution.
                Or the first degrees of freedom when using f distribution
                DEFAULT = 1   (if "t" distribution chosen)
                DEFAULT = 10  (if "f" distribution chosen)
      df2     : Second degrees of freedom when using f distribution
                DEFAULT = 100
      rate    : Used for exponential Distribution
                DEFAULT = 1
      res     : integer. Resolution of the plot (measured as the number of
                data points along the x axis)
                Not implemented for Poisson distribution yet.
                DEFAULT = 100 if using normal distribution
    returndf : should it return a dataframe of the x and y values?
                DEFAULT = FALSE
    primary   : boolean. Whether to plot as primary plot using plot() or
                 append to an exisitng plot using points()
                 DEFAULT = TRUE
    showmean  : Show a vertical line highlihgting mean of the distribution?
                 DEFAULT = False
      plower : numeric. A quantile used to calculate the lower end of the
                x axis to plot. eg, if a value of 0.25 is used, then the x
                axis will start at the 25th percentile of the distribution.
                DEFAULT = 0.0001
      pupper : numeric. quantile used to calculate the upper end of the
                x axis to plot.
                DEFAULT = 0.9999
    ...       : other parameters to pass onto the plot
    ===========================================================================
    """
    # TODO: implement shading of confidence intervals
    # TODO: implement other distributiuons
    # TODO: Check the data types of the inputs
    # TODO: Add option to draw exponential distribution using either lambda OR 
    #       the mean (where mean = 1/lambda) or sd (sd=1/lambda). But give
    #       preference in this order (lambda, mean, sd) if more than one of 
    #       those arguments is given.  
    # TODO: currently the vertical line is plotting median not mean
    # TODO: implement show.mean option
    #-------------------------------------------------------------------------
    #                                               Handle Normal Distribution
    #-------------------------------------------------------------------------
    if (dist=="normal"):
        print("TODO: implement Normal curve")
     
    #-------------------------------------------------------------------------
    #                                                    Handle t Distribution
    #-------------------------------------------------------------------------
    elif (dist=="t"):
        pass
     
    #-------------------------------------------------------------------------
    #                                                  Handle exp Distribution
    #-------------------------------------------------------------------------
    elif (dist=="exp"):
        pass
    
    #-------------------------------------------------------------------------
    #                                              Handle Poisson Distribution
    #-------------------------------------------------------------------------
    elif (dist=="poisson"):
        pass
    
    #-------------------------------------------------------------------------
    #                                             Handle Binomial Distribution
    #-------------------------------------------------------------------------
    elif (dist=="binomial"):
        #TODO: check the data types of the inputs
        if n == None: n = 1
        if p == None: p = 0.5
        #x_min = qbinom(plower, size=n, prob=p)
        #x_max = qbinom(pupper, size=n, prob=p)
        #x = range(int(round(x_min)), int(round(x_max)) + 1)
        x = range(0, n + 1)
        y = dbinom(x, n, prob=p)

        title = "Binomial Distribution with\n n={} and p={}".format(n,p)
        plt.bar(x, y, width=1,
                alpha=0.5,
                color='b', edgecolor="#FF0000",
                align="center")
        plt.xticks(x)               # only show tick labels for actual values
        plt.xlim([-0.5, n + 0.5])   # xlimits to fit entire plot snugly

        plt.xlabel('Number of Successes out of {} trials'.format(n))
        plt.ylabel('probability')
        plt.title(title)

        plt.show()

        # TODO: create a vertical line for the mean
    
    #-------------------------------------------------------------------------
    #                                 Return the dataframe if it was requested
    #-------------------------------------------------------------------------
    #if (return.df):
    #    return(data.frame(x, y))
     
    else:
        pass


if __name__ == '__main__':
    print("Plot convenience package")