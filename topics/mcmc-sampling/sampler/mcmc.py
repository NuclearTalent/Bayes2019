#!/usr/bin/env python

from abc import ABC, abstractmethod
import numpy as np

class MCMC(ABC):
    """
    An abstract sampler object that implements various helper functions.
    This class should be compatible with the abstract Sampler class from emcee
    https://emcee.readthedocs.io/en/stable/

    :param dim:
        The number of dimensions in the parameter space.

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

    def __init__(self, dim, lnpostfn, args=[], kwargs={}):
        self.dim = dim
        self.lnpostfn = lnpostfn
        self.args = args
        self.kwargs = kwargs

        # Create chain
        self.chain_object = Chain(dim)

    @property
    def acceptance_fraction(self):
        """
        The fraction of proposed steps that were accepted.
        Function name chosen for compatibility with emcee.

        """
        return self.chain_object.acceptance_rate

    @property
    def chain(self):
        """
        A pointer to the Markov chain.
        Function name chosen for compatibility with emcee.

        """
        return self.chain_object.get_chain

    @property
    def flatchain(self):
        """
        Alias of ``chain`` provided for compatibility.
        Function name chosen for compatibility with emcee.

        """
        return self.chain_object.get_chain
    
    @property
    def lnprobability(self):
        """
        A list of the log-probability values associated with each step in
        the chain.
        Function name chosen for compatibility with emcee.

        """
        return self.chain_object.get_lnprobs

    def get_lnprob(self, p):
        """Return the log-probability at the given position.
        Function name chosen for compatibility with emcee.

        """
        if np.isnan(self.lnpostfn(p, *self.args, **self.kwargs)):
            raise ValueError('NaN encountered in lnposterior')

        # OK, RETURN LN OF POSTERIOR
        return self.lnpostfn(p, *self.args, **self.kwargs)

    @property
    def acor(self):
        return self.get_autocorr_time()

    def get_autocorr_time(self, window=50):
        raise NotImplementedError("The autocorrelation method is not implemented in the superclass."
                                  "Can be implemented in subclasses.")

    def reset(self):
        """
        Clear ``chain``, ``lnprobability`` and the bookkeeping parameters.

        """
        
        # Create chain without any samples
        # Clear the chain list of log-probability values
        self.chain_object = Chain(self.dim)
        self._last_run_mcmc_result = None


    def run_mcmc(self, pos0, Nsteps, **kwargs):
        """
        Iterate :func:`sample` for ``N`` iterations and return the result.

        :param pos0:
            The initial position vector.  Can also be None to resume from
            where :func:``run_mcmc`` left off the last time it executed.

        :param Nsteps:
            The number of steps to run.

        :param kwargs: (optional)
            Other parameters that are directly passed to :func:`sample`.

        This returns the results of the final sample in whatever form
        :func:`sample` yields.  Usually, that's:
        ``pos``, ``lnprob``, ``rstate``
        """
        if pos0 is None:
            if self._last_run_mcmc_result is None:
                raise ValueError("Cannot have pos0=None if run_mcmc has never "
                                 "been called.")
            pos0 = self._last_run_mcmc_result[0]

        for results in self.sample(pos0, iterations=Nsteps,  **kwargs):
            pass

        # store so that the ``pos0=None`` case will work. 
        self._last_run_mcmc_result = results

        return results

    @abstractmethod
    def sample(self, *args, **kwargs):
        raise NotImplementedError("The sampling routine must be implemented "
                                  "by subclasses")

        

class Chain(ABC):
    """
    An abstract chain object that implements various helper functions.
    This chain object could be redefined for ensamble samplers with multiple chains.

    :param dim:
        The number of dimensions in the parameter space.

    """

    def __init__(self, dim):
        self.dim = dim
        self.chain = np.empty((0, self.dim))
        self.lnprobs = np.empty((0, 1))
        self.n_accepted = 0
        self.index = -1

    def accept(self, position,lnprob):
        self.chain[self.index+1, :] = position
        self.lnprobs[self.index+1, :] = lnprob
        self.n_accepted += 1
        self.index += 1

    def reject(self):
        self.chain[self.index+1, :] = self.head
        self.lnprobs[self.index+1, :] = self.lnprobs_head
        self.index += 1

    @property
    def head(self):
        return self.chain[self.index, :]

    @property
    def lnprobs_head(self):
        return self.lnprobs[self.index, :]

    @property
    def get_chain(self):
        return self.chain

    @property
    def get_lnprobs(self):
        return self.lnprobs

    def extend(self, n):
        self.chain = np.concatenate((self.chain, np.zeros((n, self.dim))))
        self.lnprobs = np.concatenate((self.lnprobs, np.zeros((n, 1))))

    @property
    def acceptance_rate(self):
        return self.n_accepted / (self.index+1)

    @property
    def dimensionality(self):
        return self.dim
