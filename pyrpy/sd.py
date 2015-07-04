from scipy.stats import tstd

# ==============================================================================
#                                                                             SD
# ==============================================================================
def sd(x, na_rm=False):
    """
    Compute the standard deviation of the values in x.

    If na_rm is set to True, then missing values are removed before computing
    the standard deviation.

    Parameters
    ----------------------------------------------------------------------------
    x : array_like
        Array of values.
    na_rm: bool, optional
        NOT IMPLEMENTED YET
        A boolean value indicating whether missing values should be
        stripped before the computation proceeds.
        Default is False

    Returns
    ----------------------------------------------------------------------------
    sd : float
        The standard deviation

    Notes
    ----------------------------------------------------------------------------
    `sd` returns the unbiased sample standard deviation. Thus it divides by
    the correction factor of (n - 1) instead of n.

    Examples
    ----------------------------------------------------------------------------
    >>> from pyrpy import *
    >>> sd(c(12,11,16,14,13,10,14,15,12))
    1.9364916731037085

    See Also
    ----------------------------------------------------------------------------
    var: Variance
    """
    # ==========================================================================
    # TODO: implement na_rm
    # TODO: consider adding option to calculate biased sample sd, dividing by n
    # TODO: consider adding trim as an argument and implementing it
    return tstd(x, limits=None, inclusive=(True, True))
