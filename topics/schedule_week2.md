<p align="right"><a href="https://nucleartalent.github.io/Bayes2019/">Return to home</a></p>

# Lectures of the second week

## Monday, June 17

### Assigning probabilities (Daniel Phillips)
* Choosing priors, Maximum Entropy
- [Keynote of first lecture [.pdf]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/assigning-probabilities/TALENT_M2a.pdf)
- [Maximizing the Entropy of Australians [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/assigning-probabilities/MaxEnt_Australians.ipynb)


### Model selection (Christian Forss&eacute;n)
- Model evidence
- Bayes factor
- Bayesian hypothesis testing
* Lecture notes in [pdf](pub/model_selection-minted.pdf) or [html](pub/model_selection-bs.html)
* [Bayesian model selection [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/model-selection/model-selection_I.ipynb)
* [Bayes in the sky: Bayesian inference and model selection in cosmology](https://arxiv.org/abs/0803.4089) by Robert Trotta.
* [Why every statistician should know about cross-validation](https://robjhyndman.com/hyndsight/crossvalidation/) blog post by Rob J Hyndman.




## Tuesday, June 18

### Assigning probabilities (2) (Daniel Phillips)
- Summary of prior choice discussion, Maximum Entropy for reconstructing functions
* [Keynote of second lecture [.pdf]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/assigning-probabilities/TALENT_T2b.pdf)


### Model selection (Dick Furnstahl)
- Recap of 2019-06-17 exercises: Prior sensitivity of model evidence
- Evidence when there is a naturalness prior
- Computational issues for evidence and alternatives
* [Scanned lecture notes [pdf]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/model-selection/pub/Lecture_T2a_rjf.pdf)
* [Bayes in the sky: Bayesian inference and model selection in cosmology](https://arxiv.org/abs/0803.4089) by Robert Trotta.
* [Bayesian model selection revisited [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/model-selection/model-selection_I_rjf.ipynb)
* [Evidence for EFT coefficients [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/model-selection/NuclearTalent/Bayes2019/blob/master/topics/Evidence_for_model_EFT_coefficients.ipynb)
* [EFT slides II [pdf]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/model-selection/EFT_slides_II.pdf)





## Wednesday, June 19

### Gaussian processes (Christian Forss&eacute;n)
- Gaussian processes as infinite-dimensional Gaussian distributions
- From parametric models to Gaussian processes
- Covariance functions
* [Scanned lecture notes [pdf]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/gaussian-processes/Lecture_W2b_cf.pdf)
* Gaussian processes - Part I [ipynb](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/gaussian-processes/GP-I.ipynb)


### Gaussian process models for regression (Christian Forss&eacute;n)
- Gaussian process emulators
* [Scanned lecture notes [pdf]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/gaussian-processes/Lecture_Th2a_cf.pdf)
* [A Bayesian Approach for Parameter Estimation and Prediction using a Computationally Intensive Model](https://arxiv.org/abs/1407.3017) by D. Higdon et al.




## Thursday, June 20

### Gaussian processes (Christian Forss&eacute;n)
- Gaussian process models for regression
- Gaussian process emulators
* [Scanned lecture notes [pdf]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/gaussian-processes/Lecture_Th2a_cf.pdf)
* [A Bayesian Approach for Parameter Estimation and Prediction using a Computationally Intensive Model](https://arxiv.org/abs/1407.3017) by D. Higdon et al.


### MCMC sampling (Dick Furnstahl)
- Visualization of Hamiltonian Monte Carlo (HMC) and the No-U-Turn Sampler (NUTS)
- Physics of HMC
- PyMC3 overview
* [Scanned lecture notes](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/mcmc-sampling/Lecture_W2a_rjf.pdf)
* [HMC visualization I (Richard McElreath)](http://elevanth.org/blog/2017/11/28/build-a-better-markov-chain/)
* [HMC visualization II (Alex Rogozhnikov)](https://arogozhnikov.github.io/2016/12/19/markov_chain_monte_carlo.html)
* [Bettencourt, *A conceptual introduction to Hamiltonian Monte Carlo*](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/mcmc-sampling/Refs/Conceptual_introduction_to_Hamiltonian_Monte_Carlo_Betancourt_1701.02434.pdf)
* [Neal, *MCMC using Hamiltonian dynamics*](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/mcmc-sampling/Refs/MCMC_using_Hamiltonian_dynamics_Neal_1206.1901.pdf)
* [PyMC3: Introduction [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/mcmc-sampling/PyMC3/PyMC3_intro.ipynb)
* [PyMC3 Docs: Getting started [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/mcmc-sampling/PyMC3/PyMC3_docs_getting_started.ipynb)
* [PyMC3 Docs: Quick start [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/mcmc-sampling/PyMC3/PyMC3_docs_api_quickstart.ipynb)
* [PyMC3 linear regression example (from Duke course)[ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/mcmc-sampling/PyMC3/Linear_regression_S15B_PyMC3.ipynb)
* [PyMC3: Rob Hicks Bayesian 8 [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/mcmc-sampling/PyMC3/Rob_Hicks_bayesian_8.ipynb) Shows a comparison between Gibbs sampling, PyMC3, and emcee plus an example of using corner with PyMC3 output.
* [Liouville theorem visualization [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/mcmc-sampling/PyMC3/Liouville_theorem_visualization.ipynb)
* [Orbital equations solved with different algorithms, including 2nd-order leapfrog [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/mcmc-sampling/PyMC3/Orbital_eqs_with_different_algorithms.ipynb)



## Friday, June 21

### Applications of Bayesian Methods in Nuclear Physics (Dick Furnstahl)

### Why Bayes is Better (3) (Daniel Phillips)
- Systematic errors: offset, normalization uncertainty, other experimental systematics, theory systematic from an EFT
* [Lecture on systematic errors [pdf]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/why-bayes-is-better/TALENT_F2a.pdf)




