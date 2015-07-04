from scipy.stats import norm

# TODO: Verify the outputs of these functions, make sure i implemented them
#       correctly


def cnorm(mean=0, sd=1, type="equal", conf=0.95):
    """
    ============================================================================
                                                                          cnorm
    ============================================================================
    Confidence region for a normal Distribution.

    USAGE:
    cnorm(mean=0, sd=1, type="equal", conf=0.95)
    dnorm(x, mean=0, sd=1, log=False)
    pnorm(q, mean=0, sd=1, lowertail=True, log=False)
    qnorm(p, mean=0, sd=1, lowertail=True, log=False)
    rnorm(n=1, mean=0, sd=1)

    :param mean (float): mean of the distribution
    :param sd (float):   standard deviation
    :param type (string): type of hypothesis test taken.
           "equal" (Default) for two tailed test
           "less" for one-tailed test where alternative hypotheis is 'less than'
           "more" for one-tailed test where alternative hypotheis is 'more than'
    :param conf (float): confidence interval used
    :return: a list with two values representing the lower and upper points that
             fit within your confidence interval.

    Examples:
    cnorm(mean=50, sd=15.5, type="equal", conf=0.99)
    cnorm(mean=50, sd=15.5, type="less", conf=0.95)
    cnorm(mean=50, sd=15.5, type="more", conf=0.90)
    ============================================================================
    """

    # Account for the different types of cutoff quantiles
    alpha = 1 - conf
    if (type == "less"):
        p_lower = alpha
        p_upper = 1.0
    elif (type == "more"):
        p_lower = 0.0
        p_upper = conf
    elif (type == "equal"):
        p_lower= alpha/2
        p_upper = 1 - (alpha/2)

    # calculate the cutoff points
    cutoff_lower = qnorm(p_lower, mean=mean, sd=sd, lowertail=True)
    cutoff_upper = qnorm(p_upper, mean=mean, sd=sd, lowertail=True)

    return [cutoff_lower, cutoff_upper]


def rnorm(n=1, mean=0, sd=1):
    """
    ============================================================================
                                                                         rnorm()
    ============================================================================
    Creates an array of random numbers from a normal distribution, where you
     can specify the mean and standard deviation.

    USAGE:
    cnorm(mean=0, sd=1, type="equal", conf=0.95)
    dnorm(x, mean=0, sd=1, log=False)
    pnorm(q, mean=0, sd=1, lowertail=True, log=False)
    qnorm(p, mean=0, sd=1, lowertail=True, log=False)
    rnorm(n=1, mean=0, sd=1)

    :param n (int):      size of the array
    :param mean (float): mean of the distribution
    :param sd (float):   standard deviation
    :return:        returns an array of random numbers

    EXAMPLES:
    rnorm()                # returns a random number from a the standard normal
                           # distribution (mean=0. sd=1)

    rnorm(10)              # returns 10 such random numbers

    rnorm(10, mean=50, sd=15.5) # returns 10 random numbers from a normal
                           # distribution with a mean of 50 and standard
                           # deviation of 15.5
    ============================================================================
    """
    return norm.rvs(loc=mean, scale=sd, size=n)


def dnorm(x, mean=0, sd=1, log=False):
    """
    ============================================================================
                                                                         dnorm()
    ============================================================================
    Density Function for the normal distribution.
    Returns the probability density value at the value x.

    USAGE:
    cnorm(mean=0, sd=1, type="equal", conf=0.95)
    dnorm(x, mean=0, sd=1, log=False)
    pnorm(q, mean=0, sd=1, lowertail=True, log=False)
    qnorm(p, mean=0, sd=1, lowertail=True, log=False)
    rnorm(n=1, mean=0, sd=1)

    :param x (float, array of floats): The value(s) of x
    :param mean (float): mean of the distribution
    :param sd (float):   standard deviation
    :param log (bool):   take the log?
    :return:        returns an array of density values
    ============================================================================
    """
    if log:
        return norm.logpdf(x, loc=mean, scale=sd)
    else:
        return norm.pdf(x, loc=mean, scale=sd)


def qnorm(q, mean=0, sd=1, lowertail=True):
    """
    ============================================================================
                                                                         qnorm()
    ============================================================================
    The quantile function for the normal distribution.
    You provide a quantile (eg q=0.75) or array of quantiles, and it returns the
    value along the normal distribution that corresponds to the qth quantile.

    USAGE:
    cnorm(mean=0, sd=1, type="equal", conf=0.95)
    dnorm(x, mean=0, sd=1, log=False)
    pnorm(q, mean=0, sd=1, lowertail=True, log=False)
    qnorm(p, mean=0, sd=1, lowertail=True, log=False)
    rnorm(n=1, mean=0, sd=1)

    :param q (float, array of floats): The quantile(s)
    :param mean (float):     mean of the distribution
    :param sd (float):       standard deviation
    :param lowertail (bool): lowertail (true), or survival (false)
    :return:        an array of the value(s) corresponding to the quantiles q
    ============================================================================
    """
    # TODO: check that q is between 0.0 and 1.0

    if lowertail:
        return norm.ppf(q=q, loc=mean, scale=sd)
    else:
        return norm.isf(q=q, loc=mean, scale=sd)


def pnorm(x, mean=0, sd=1, lowertail=True, log=False):
    """
    ============================================================================
                                                                        pnorm()
    ============================================================================
    The cumulative distribution function for the normal distribution.
    You provide a value along the normal distribution (eg x=3) or array of
    values, and it returns what proportion of values lie below it (the quantile)

    Alternatively, if you select lowertail=False, it returns the proportion of
    values that are above it.

    USAGE:
    cnorm(mean=0, sd=1, type="equal", conf=0.95)
    dnorm(x, mean=0, sd=1, log=False)
    pnorm(q, mean=0, sd=1, lowertail=True, log=False)
    qnorm(p, mean=0, sd=1, lowertail=True, log=False)
    rnorm(n=1, mean=0, sd=1)

    :param x (float, array of floats): The values along the distribution.
    :param mean (float):     mean of the distribution
    :param sd (float):       standard deviation
    :param lowertail (bool): are you interested in what proportion of values
                             lie beneath x? or above x (false)?
    :param log (bool):       take the log?
    :return:        an array of quantiles() corresponding to the values in x
    ============================================================================
    """
    if lowertail and not log:
        return norm.cdf(x, loc=mean, scale=sd)
    elif not lowertail and not log:
        return norm.sf(x, loc=mean, scale=sd)
    elif lowertail and log:
        return norm.logcdf(x, loc=mean, scale=sd)
    else:
        return norm.logsf(x, loc=mean, scale=sd)

