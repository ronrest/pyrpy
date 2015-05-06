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
                                                                           pyRpy
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

import numpy as np
from scipy.misc import comb
from scipy.misc import factorial as spfactorial

__all__ = ["mean", "sort", "c", "nck", "choose", "npk", "factorial"]

def sort(x, decreasing=False, nalast=None):
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