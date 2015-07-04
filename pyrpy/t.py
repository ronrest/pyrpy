from scipy.stats import t

__author__ = 'Ronny Restrepo'
__all__ = ["ct", "rt", "dt", "qt", "pt"]


# TODO: Verify the outputs of these functions, make sure i implemented them
#       correctly


# ==============================================================================
#                                                                             CT
# ==============================================================================
def ct(df=0, loc=0, scale=1, type="equal", conf=0.95):
    """
    Confidence region for a t Distribution.

    ARGS:
    ---------------------
    :param df (int):
        Degrees of Freedom
    :param loc (float):
        location
    :param scale (float):
        scale
    :param type (string):
        type of hypothesis test taken.
           "equal" (Default) for two tailed test
           "less" for one-tailed test where alternative hypotheis is 'less than'
           "more" for one-tailed test where alternative hypotheis is 'more than'
    :param conf (float):
        confidence interval used.
        (default is 0.95)

    RETURN:
    ---------------------
    :return:
        a list with two values representing the lower and upper points that
             fit within your confidence interval.

    EXAMPLES:
    ---------------------
    ct(df=15, conf=0.99)
    ct(df=15, type="less", conf=0.99)
    ct(df=15, type="more", conf=0.90)
    """
    # ==========================================================================
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
    cutoff_lower = qt(p_lower, df=df, lowertail=True, loc=loc, scale=scale)
    cutoff_upper = qt(p_upper, df=df, lowertail=True, loc=loc, scale=scale)

    return [cutoff_lower, cutoff_upper]

# ==============================================================================
#                                                                             RT
# ==============================================================================
def rt(n=1, df=1, loc=0, scale=1, ncp=None):
    """
    Creates an array of random numbers from a t distribution, where you
    can specify the number of items, and the degrees of freedom.

    ARGS:
    ---------------------
    :param n (int):
        size of the array
    :param df (float):
        degrees of freedom
    :param loc: array_like, optional
        location parameter (default=0)
    :param scale: float, optional
        scale (default=1)
    :param ncp (float):
        non-centrality parameter delta.
        Currently not implemented.

    RETURN:
    ---------------
    :return:
        returns an array of random numbers

    EXAMPLES:
    --------------------
    rt()                # returns a random number from a the t
                        # distribution (df=1)

    rt(10)              # returns 10 such random numbers

    rt(10, df=15)       # returns 10 random numbers from a t
                        # distribution with 15 degrees of freedom.
    """
    # ==========================================================================
    return t.rvs(df=df, loc=loc, scale=scale, size=n)

# ==============================================================================
#                                                                             DT
# ==============================================================================
def dt(x, df=1, loc=0, scale=1, ncp=None, log=False):
    """
    Density Function for the t distribution.
    Returns the probability density value at the value x.

    ARGS:
    ---------------
    :param x (float, array of floats):
        The value(s) of x
    :param df (float):
        degrees of freedom
    :param loc: array_like, optional
        location parameter (default=0)
    :param scale: float, optional
        scale (default=1)
    :param ncp (float):
        non-centrality parameter delta.
        Currently not implemented.
    :param log (bool):
        take the log?


    RETURN:
    ---------------
    :return:        returns an array of density values
    """
    # ==========================================================================
    if log:
        return t.logpdf(x, df=df, loc=0, scale=1)
    else:
        return t.pdf(x, df=df, loc=0, scale=1)


# ==============================================================================
#                                                                             QT
# ==============================================================================
def qt(q, df=1, loc=0, scale=1, ncp=None, lowertail=True, log=False):
    """
    The quantile function for the t distribution.
    You provide a quantile (eg q=0.75) or array of quantiles, and it returns the
    value along the t distribution that corresponds to the qth quantile.

    So using a value of q=0.30 means that 30% of the values are below the
    returned value. So it essentially gives us the cut off point for the lowest
    30% of values. If you want the cutoff point for the top 30% of values, then
    use lowertail=False.

    ARGS:
    ---------------
    :param q (float, array of floats):
        The quantile(s)
    :param df (float):
        degrees of freedom
    :param loc: array_like, optional
        location parameter (default=0)
    :param scale: float, optional
        scale (default=1)
    :param ncp (float):
        non-centrality parameter delta.
        Currently not implemented.
    :param lowertail (boolean):
        Lower tail?
    :param log: (boolean)
        use log?
        Currently not implemented
    RETURN:
    ---------------
    :return:        an array of the value(s) corresponding to the quantiles q
    """
    # ==========================================================================
    if log:
        raise NotImplementedError("Log option is not implemented yet.")
    elif lowertail:
        return t.ppf(x=q, df=df, loc=loc, scale=scale)
    else:
        return t.isf(q=q, df=df, loc=loc, scale=scale)


# ==============================================================================
#                                                                             PT
# ==============================================================================
def pt(x, df=1, loc=0, scale=1, ncp=None, lowertail=True, log=False):
    """
    The cumulative distribution function for the t distribution.
    You provide a value along the t distribution (eg x=3) or array of
    values, and it returns what proportion of values lie below it (the quantile)

    Alternatively, if you select lowertail=False, it returns the proportion of
    values that are above it.

    ARGS:
    ---------------
    :param x (float, array of floats):
        The values along the distribution.
    :param df (float):
        degrees of freedom
    :param loc: array_like, optional
        location parameter (default=0)
    :param scale: float, optional
        scale (default=1)
    :param ncp (float):
        non-centrality parameter delta.
        Currently not implemented.
    :param lowertail (bool):
        are you interested in what proportion of values lie beneath x? or
        above x (False)?
    :param log (boolean):
        Use log scale?

    RETURN:
    ---------------
    :return:
        an array of quantiles() corresponding to the values in x
    """
    if lowertail and not log:
        return t.cdf(x, df=df, loc=loc, scale=scale)
    elif not lowertail and not log:
        return t.sf(x, df=df, loc=loc, scale=scale)
    elif lowertail and log:
        return t.logcdf(x, df=df, loc=loc, scale=scale)
    else:
        return t.logsf(x, df=df, loc=loc, scale=scale)


