# Copyright (c) Ronny Restrepo.  All rights reserved
#
# Disclaimer
#
# This software is provided "as-is".  There are no expressed or implied
# warranties of any kind, including, but not limited to, the warranties
# of merchantability and fitness for a given application.  In no event
# shall Ronny Restrepo be liable for any direct, indirect, incidental,
# special, exemplary or consequential damages (including, but not limited
# to, loss of use, data or profits, or business interruption) however
# caused and on any theory of liability, whether in contract, strict
# liability or tort (including negligence or otherwise) arising in any way
# out of the use of this software, even if advised of the possibility of
# such damage.
#



"""
################################################################################
                                                                           pyrpy
################################################################################

Array Functions
---------------
    autosummary::
   :toctree: generated/
    c

Sorting and Arranging
---------------
    autosummary::
   :toctree: generated/
    sort

Central Tendency
----------------
.. autosummary::
   :toctree: generated/
    mean
    mode
    median

Deviation
-----------------
.. autosummary::
   :toctree: generated/
    sd

Moments
-------
.. autosummary::
   :toctree: generated/
    skew
    kurtosis


Combinatorics
-------
.. autosummary::
   :toctree: generated/
    factorial
    choose
    nck
    npk

"""
from __future__ import division, print_function, absolute_import

__author__ = 'Ronny Restrepo'
__all__ = ["mean", "sd", "sort", "c", "nck", "choose", "npk", "factorial"]

# selected functions from files
from pyrpy.norm import cnorm, rnorm, qnorm, pnorm, dnorm
from pyrpy.binom import cbinom, rbinom, qbinom, pbinom, dbinom
from pyrpy.t import ct, rt, qt, pt, dt

# Plots
from pyrpy.plot import plot
from pyrpy.plot_distribution import plot_distribution

import numpy as np
from scipy.misc import comb
from scipy.misc import factorial as spfactorial
from scipy.stats import tmean, tstd


# ==============================================================================
#                                                                       TEMPLATE
# ==============================================================================
def _template(x, arg2, arg3):
    """
    One sentence Description.

    Detailed description here. Can be several sentences or paragraphs long.

    Parameters
    ----------------------------------------------------------------------------
    x : array_like
        Array of values.
    arg2 : None or int, optional
        Description of arg2. When this value is None (default), then something
        happens. If int, the something.
    arg3 : (lower, upper), optional
        A tuple consisting of the (lower flag, upper flag).  These flags
        determine the lower or upper limits. The default value is (0, 100).

    Returns
    ----------------------------------------------------------------------------
    tmean : float
        Description of output.

    Notes
    ----------------------------------------------------------------------------
    `template` behaves in such and such away that you should be aware of in such
     and such circumstances. Just to let you know.

    Examples
    ----------------------------------------------------------------------------
    >>> from pyrpy import *
    >>> template([1,2,3,4], arg2=4, arg3=(2,5))
    some out put here

    See Also
    ----------------------------------------------------------------------------
    median: Median
    mode: Mode
    """
    pass


# ##############################################################################
#                                                         MEASURES OF CENTRALITY
# ##############################################################################

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


# ##############################################################################
#                                                             MEASURES OF SPREAD
# ##############################################################################


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


def sort(x, decreasing=False, na_last=None):
    """
    ============================================================================
                                                                            SORT
    ============================================================================
    Sorts an array or list of items.

    :param x: list or array of numbers that you want to sort.
    :param decreasing: bool. Should you order in descending order?
    :param nalast: Handling of missing values. If True, they are placed last.
                   if False, they are placed first. If None, they are removed.
                   NOTE: this has not been implemented yet.
    :return: The list with the items ordered.
    ============================================================================
    """
    # TODO: implement nalast option
    return c(sorted(x, reverse=decreasing))


def c(*args):
    """
    ============================================================================
                                                                               C
    ============================================================================
    Creates an array (vector)
    NOTE: Do not try concatenating arrays using this. That feature has not been
    implemented yet. You will end up with a multidimensional array if you do.

    :param args: The elements of your array
    :return: An array
    ============================================================================
    """
    # TODO: implement concatenation of arrays in c()
    return np.array(args)


# Permutations and Combinations
def nck(n, k, exact=False):
    """
    ============================================================================
                                                                             NCK
    ============================================================================
    n choose k

    :param n (int):
    :param k (int):
    :param exact (bool):
    :return (int, long): integer for smaller numbers, Long for larger numbers
    ============================================================================
    """
    return(int(round(comb(n, k, exact=exact))))

def choose(n, k, exact=False):
    """
    ============================================================================
                                                                          CHOOSE
    ============================================================================
    n choose k

    :param n (int):
    :param k (int):
    :param exact (bool):
    :return (int, long): integer for smaller numbers, Long for larger numbers
    ============================================================================
    """
    return(int(round(comb(n, k, exact=exact))))


def npk(n, k, exact=False):
    """
    ============================================================================
                                                                             NPK
    ============================================================================
    n perm k. Permutations

    :param n (int):
    :param k (int):
    :param exact (bool):
    :return (int, long): integer for smaller numbers, Long for larger numbers
    ============================================================================
    """
    return(int(round(nck(n, k, exact=exact) * factorial(k, exact))))


def factorial(n, exact=False):
    """
    ============================================================================
                                                                       FACTORIAL
    ============================================================================
    factorial
    :param n:
    :param exact:
    :return (int, long): integer for smaller numbers, Long for larger numbers
    ============================================================================
    """
    return(int(round(spfactorial(n, exact))))


# TODO: make sqrt() automatically load up by implementing a call to math.sqrt()

if __name__ == '__main__':
    print("Ahoy a Hoy!")