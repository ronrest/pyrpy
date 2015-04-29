"""
################################################################################
                                                                           pyRpy
################################################################################
"""
__author__ = 'Ronny Restrepo'
from scipy.stats import binom

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
    dbinom(x, size, prob=0.5, log=FALSE)
    pbinom(q, size, prob, lower.tail = TRUE, log.p = FALSE)
    qbinom(p, size, prob, lower.tail = TRUE, log.p = FALSE)
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
    dbinom(x, size, prob=0.5, log=FALSE)
    pbinom(q, size, prob, lower.tail = TRUE, log.p = FALSE)
    qbinom(p, size, prob, lower.tail = TRUE, log.p = FALSE)
    rbinom(n=1, size=1, prob=0.5)

    :param x:       int. The number of successes
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



if __name__ == '__main__':
    print("Ahoy a Hoy!")

    rbinom(10, size=3)