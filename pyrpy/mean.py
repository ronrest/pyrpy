from scipy.stats import tmean

# ==============================================================================
#                                                                           MEAN
# ==============================================================================
def mean(x, trim=0, na_rm=False):
    """
    Compute the trimmed mean.
    This function finds the arithmetic mean of given values, ignoring values
    outside the given `limits`.

    Parameters
    ----------------------------------------------------------------------------
    x : array_like
        Array of values.
    trim: int, optional
        NOT IMPLEMENTED YET
        The fraction (0 to 0.5) of observations to be trimmed from each end of
        x before the mean is computed. Values of trim outside that range are
        taken as the nearest endpoint.
        Default is 0.
    na_rm: bool, optional
        NOT IMPLEMENTED YET
        A boolean value indicating whether missing values should be
        stripped before the computation proceeds.
        Default is False

    Returns
    ----------------------------------------------------------------------------
    mean : float
        The arithmetic mean

    Examples
    ----------------------------------------------------------------------------
    >>> from pyrpy import *
    >>> mean(c(5, 10, 6, 9, 7, 8))
    7.5

    See Also
    ----------------------------------------------------------------------------
    median: Median
    mode: Mode
    """
    # ==========================================================================
    # TODO: implement trim
    # TODO: implement na_rm
    return tmean(x, limits=None, inclusive=(True, True))

