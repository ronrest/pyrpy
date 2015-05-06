"""====================================================
                    DESCRIPTION

=======================================================
"""
__author__ = 'Ronny Restrepo'

from scipy.stats import binom

def cbinom(size=1, prob=0.5, type="equal", conf=0.95):
    """
    ============================================================================
                                                                          cbinom
    ============================================================================
    Confidence region for a binomial Distribution.

    Args:
    :param size (int): number of trials for the binomial distribution.
    :param p (float): probability of success per trial
    :param type (string): type of hypothesis test taken.
           "equal" (Default) for two tailed test
           "less" for one-tailed test where alternative hypotheis is 'less than'
           "more" for one-tailed test where alternative hypotheis is 'more than'
    :param conf (float): confidence interval used
    :return: a list with two values representing the lower and upper points that
             fit within your confidence interval.

    Examples:
    cbinom(size=100, p=0.7, type="equal", conf=0.99)
    cbinom(size=15, p=0.9, type="less", conf=0.95)
    cbinom(size=30, p=0.4, type="more", conf=0.90)
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
    cutoff_lower = qbinom(p_lower, size=size, prob=prob, lowertail=True)
    cutoff_upper = qbinom(p_upper, size=size, prob=prob, lowertail=True)

    return([cutoff_lower, cutoff_upper])


def rbinom(n=1, size=1, prob=0.5):
    """
    ============================================================================
                                                                        rbinom()
    ============================================================================
    Creates an array of random numbers from a binomial distribution of "size"
    number of trials, and probability of success "prob" for each trial.

    Can be thought of as returning "n" random number of 'successes' out of a set
    of trials of size "size".

    USAGE:
    dbinom(x, size, prob=0.5, log=False)
    pbinom(q, size, prob=0.5, lowertail=True, log=False)
    qbinom(p, size, prob=0.5, lowertail=True, log=False)
    rbinom(n=1, size=1, prob=0.5)

    :param n:     int. size of the array
    :param size:  int. Number of trials
    :param prob:  float. probability of success for each trial
    :return:      returns an array of random numbers

    EXAMPLES:
    rbinom()                # returns eg a flip of a fair coin
    rbinom(10)              # returns eg 10 flips of a fair coin
    rbinom(10, prob=0.7)    # returns eg 10 flips of an unfair coin P(Head)= 0.7


    ============================================================================
    """
    # Note, scipy flips meaning of n and size
    return binom.rvs(n=size, p=prob, size=n)


def dbinom(x, size=1, prob=0.5, log=False):
    """
    ============================================================================
                                                                        dbinom()
    ============================================================================
    Density Function for the binomial distribution.
    Returns the probability of getting "x" successes out of "size" number of
    trials, given a probability of "prob" for each success.

    USAGE:
    dbinom(x, size, prob=0.5, log=False)
    pbinom(q, size, prob=0.5, lowertail=True, log=False)
    qbinom(p, size, prob=0.5, lowertail=True, log=False)
    rbinom(n=1, size=1, prob=0.5)

    :param x:       int. or array of ints. The number of successes
    :param size:    int. Number of trials
    :param prob:    float. Probability of a success
    :param log:     bool. take the log?
    :return:
    ============================================================================
    """
    if log:
        # note, scipy flips meaning of n and size
        return binom.logpmf(x, n=size, p=prob, loc=0)
    else:
        # note, scipy flips meaning of n and size
        return binom.pmf(x, n=size, p=prob)


def qbinom(q, size=1, prob=0.5, lowertail=True):
    """
    ============================================================================
                                                                        qbinom()
    ============================================================================
    The quantile function for the binomial distribution.
    You provide a quantile (eg q=0.75) or array of quantiles, and it returns the
    value along the binomial distribution that corresponds to the qth quantile.

    USAGE:
    dbinom(x, size, prob=0.5, log=False)
    pbinom(q, size, prob=0.5, lowertail=True, log=False)
    qbinom(p, size, prob=0.5, lowertail=True)
    rbinom(n=1, size=1, prob=0.5)

    :param q:       float. or array of floats. The quantile ()
    :param size:    int. Number of trials
    :param prob:    float. Probability of a success
    :param log:     bool. take the log?
    :return:        an array of the value(s) corresponding to the quantiles q
    ============================================================================
    """
    # TODO: BUG: qbinom(0, size=11, prob=0.3) gives -1. It should be 0
    # TODO: check that q is between 0.0 and 1.0

    if lowertail:
        return binom.ppf(q=q, n=size, p=prob)
    else:
        return binom.isf(q=q, n=size, p=prob)


def pbinom(x, size=1, prob=0.5, lowertail=True, log=False):
    """
    ============================================================================
                                                                        pbinom()
    ============================================================================
    The cumulative distribution function for the binomial distribution.
    You provide a value along the binomial distribution (eg x=3) or array of
    values, and it returns what proportion of values lie below it (the quantile)

    Alternatively, if you select lowertail=False, it returns the proportion of
    values that are above it.

    USAGE:
    dbinom(x, size, prob=0.5, log=False)
    pbinom(x, size, prob=0.5, lowertail=True, log=False)
    qbinom(q, size, prob=0.5, lowertail=True)
    rbinom(n=1, size=1, prob=0.5)

    :param x:       int. or array of ints. The values along the distribution.
    :param size:    int. Number of trials
    :param prob:    float. Probability of a success
    :param lowertail bool. are you interested in what proportion of values lie
                     beneath x?
    :param log:     bool. take the log?
    :return:        an array of quantiles() corresponding to the values in x
    ============================================================================
    """
    if lowertail and not log:
        return binom.cdf(x, n=size, p=prob)
    elif not lowertail and not log:
        return binom.sf(x, n=size, p=prob)
    elif lowertail and log:
        return binom.logcdf(x, n=size, p=prob)
    else:
        return binom.logsf(x, n=size, p=prob)

if __name__ == '__main__':
    print("This is the distributions module")