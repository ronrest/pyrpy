"""
################################################################################
                                                                           pyRpy
################################################################################
"""
__author__ = 'Ronny Restrepo'

def sort(x, decreasing=False, nalast=None):
    """
    ============================================================================
                                                                          SORT()
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
    return sorted(x, reverse=decreasing)



if __name__ == '__main__':
    print("Ahoy a Hoy!")