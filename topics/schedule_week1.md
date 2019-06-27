<p align="right"><a href="https://nucleartalent.github.io/Bayes2019/">Return to home</a></p>

# Lectures of the first week

## Monday, June 10

### Introduction, Bayes theorem (Daniel Phillips)

* [Lecture [pdf]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/basics-of-bayesian-statistics/TALENT_M1a.pdf)
* [Simple sum and product rule [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/basics-of-bayesian-statistics/simple_sum_product_rule.ipynb) [(key ipynb)](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/basics-of-bayesian-statistics/simple_sum_product_rule_KEY.ipynb)
* [Exploring pdfs [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/basics-of-bayesian-statistics/Exploring_pdfs.ipynb)
* [Bayesian updating: Coinflipping [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/basics-of-bayesian-statistics/Bayesian_updating_coinflip_interactive.ipynb)
* [Medical examples [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/basics-of-bayesian-statistics/medical_example_by_Bayes.ipynb) [(key ipynb)](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/basics-of-bayesian-statistics/medical_example_by_Bayes_KEY.ipynb)


### Bayesian parameter estimation (Dick Furnstahl)
- Overview of parameter estimation, frequentist vs. bayesian
- Examples: parameters of Gaussian noise, fitting a straight line
* [Scanned lecture notes](Lecture_M1b_rjf.pdf)
* [Intro notebook revisited [ipynb]](parameter_estimation_in_bayesTALENT_intro.ipynb)
* [Parameter estimation: fitting a straight line [ipynb]](parameter_estimation_fitting_straight_line_I.ipynb)


### Jupyter notebooks and python basics
This directory contains notebooks introducing the basics of python programming and jupyter notebooks
* [Jupyter and Python intro 01 [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/jupyter-and-python-basics/TALENT_Jupyter_Python_intro_01.ipynb)
* [Jupyter and Python intro 02 [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/jupyter-and-python-basics/TALENT_Jupyter_Python_intro_02.ipynb)

### Introduction to git (John Bower, Christian Drischler)

#### Initial configuration

    git config --global user.name "Oski Bear"
    git config --global user.email obear@example.com
    
Use here your `name` as well as your `email`.

####  Discussed commands relevant for this course

* `git status`
* `git branch`
* `git merge`
* `git log`
* `git checkout [-b]`
* `git pull`
* `git clone`
* `git commit`
* `git reset [--hard]`
* ...


## Tuesday, June 11

### Bayesian updating, Bayesian convergence (Daniel Phillips)
* [Lecture [pdf]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/basics-of-bayesian-statistics/TALENT_T1a.pdf)

### Bayesian Parameter Estimation (Dick Furnstahl)
- Central limit theorem
- Correlations and the likelihood / posterior
- Amplitude of a signal in the presence of background
* [Scanned lecture notes](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/bayesian-parameter-estimation/Lecture_T1b_rjf.pdf)
* [Exploring pdfs [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/basics-of-bayesian-statistics/Exploring_pdfs.ipynb)
* [Signal and background [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/bayesian-parameter-estimation/amplitude_in_presence_of_background.ipynb)




## Wednesday, June 12

### MCMC sampling (Dick Furnstahl)
- Why Markov Chain Monte Carlo (MCMC)?
- Metropolis-Hastings algorithm
- Visualization of MCMC
- Poisson distribution example
* [Scanned lecture notes](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/mcmc-sampling/Lecture_W1a_rjf.pdf)
* [Visualization of MCMC sampling (Richard McElreath)](http://elevanth.org/blog/2017/11/28/build-a-better-markov-chain/)
* [Metropolis Poisson example [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/mcmc-sampling/Metropolis_Poisson_example.ipynb)


### Why Bayes is Better (1) (Christian Forss&eacute;n)
- Prior information
- Marginalization
* [Scanned lecture notes [pdf]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/why-bayes-is-better/Lecture_W1b_cf.pdf)
* [Why Bayes is Better I [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/why-bayes-is-better/why_bayes_is_better_I.ipynb)
* [Fitting a straight line II [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/why-bayes-is-better/parameter_estimation_fitting_straight_line_II.ipynb)
* [A Bayesian billiard game [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/why-bayes-is-better/bayes_billiard.ipynb)




## Thursday, June 13

### Bayesian Parameter Estimation (Dick Furnstahl)
- Recap of signal + background
- Error probagation for multivariate Gaussians 
- Maximum likelihood in linear algebra form
* [Scanned lecture notes](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/bayesian-parameter-estimation/Lecture_Th1a_rjf.pdf)
* [Signal and background recap [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/bayesian-parameter-estimation/amplitude_in_presence_of_background_RECAP.ipynb)
* [Data analysis recipes: Fitting a model to data](https://arxiv.org/abs/1008.4686) --- article from Hogg, Bovy, and Lang about real-world fitting (many interesting annotations!).

### MCMC sampling (Christian Forss&eacute;n)
- Assessing convergence of MCMC simulations
- Multimodal distributions and parallel tempering
* [Scanned lecture notes](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/mcmc-sampling/Lecture_Th1b_cf.pdf)
* [MCMC diagnostics [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/mcmc-sampling/MCMC-diagnostics.ipynb)
* [MCMC PT [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/mcmc-sampling/MCMC-PT.ipynb)
  




## Friday, June 14

### Introduction to EFT and why Bayesian methods are particularly relevant there (Dick Furnstahl)
* [ISNET-6 website](https://indico.gsi.de/event/7534/) --- Uncertainty Quantification at the Extremes (Darmstadt, 8-12 October, 2019).
* [Talk on *Bayesian Statistics for Effective Field Theories* [pdf]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/Fridays/MSU_statistics_conference_2018_Furnstahl_pdf.pdf)


### Why Bayes is Better (2) (Christian Forss&eacute;n)
- Error propagation
- Dealing with outliers
* [Scanned lecture notes [pdf]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/why-bayes-is-better/Lecture_F1a_cf.pdf)
* [Why Bayes is Better II [ipynb]](https://github.com/NuclearTalent/Bayes2019/blob/master/topics/why-bayes-is-better/why_bayes_is_better_II.ipynb)




