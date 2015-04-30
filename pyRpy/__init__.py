"""
################################################################################
                                                                           pyRpy
################################################################################
"""
__author__ = 'Ronny Restrepo'
import numpy as np

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


if __name__ == '__main__':
    print("Ahoy a Hoy!")