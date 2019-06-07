#!/usr/bin/env python

from .mcmc import MCMC
import numpy as np
from numpy.random import multivariate_normal

class MHSAMPLER(MCMC):
    """
    The most basic possible Metropolis-Hastings style MCMC sampler

    :param cov:
        The covariance matrix to use for the proposal distribution.

    :param dim:
        Number of dimensions in the parameter space.

    :param lnpostfn:
        A function that takes a vector in the parameter space as input and
        returns the natural logarithm of the posterior probability for that
        position.

    :param args: (optional)
        A list of extra positional arguments for ``lnpostfn``. ``lnpostfn``
        will be called with the sequence ``lnpostfn(p, *args, **kwargs)``.

    :param kwargs: (optional)
        A list of extra keyword arguments for ``lnpostfn``. ``lnpostfn``
        will be called with the sequence ``lnpostfn(p, *args, **kwargs)``.

    """
        
    def __init__(self, cov, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert len(cov) == self.dim, "Proposal distribution for MH-sampler must be of the correct dimension!"
        self.cov = cov

    def get_autocorr_time(self):
        raise NotImplementedError("The get_autocorr_time method is not yet implemented.")
    
    def sample(self, p0, iterations=1):
        """
        Advances the chain ``iterations`` steps as an iterator

        :param p0:
            The initial position vector.

        :param iterations: (optional)
            The number of steps to run.

        At each iteration, this generator yields:

        * ``pos`` - The current positions of the chain in the parameter
          space.

        * ``lnprob`` - The value of the log posterior at ``pos`` .

        * ``rstate`` - The current state of the random number generator.
                       Kept for compatibility with emcee.

        """

        raise NotImplementedError("The sample method is not yet implemented.")
    
