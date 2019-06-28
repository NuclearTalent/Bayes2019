{% include mathjax.html %}

# Discussion topics and frequently asked questions

Here we collect questions on Bayesian statistics and its application to nuclear physics problems. Some of these are also asked in other Jupyter notebooks. Participants are strongly encouraged to try these questions and propose answers, and also to suggest new questions to be added. 

## <a name="Categories">Categories</a> 

- <a href="#Basics">Bayesian basics</a>    
- <a href="#PDFs">All about pdfs</a>    
- <a href="#Frequentist">Bayesian vs. Frequentist</a>
- <a href="#ParamEst">Parameter estimation</a>
- <a href="#Sampling">Sampling</a>
- <a href="#Selection">Model selection</a>    
- <a href="#Checking">Model checking</a>    
- <a href="#GPs">Gaussian processes</a>    
- <a href="#Machine">Bayesian machine learning</a>
- <a href="#Refs">References, links, etc.</a>

## <a name="Basics">Bayesian basics</a>

  
1. What are the best references for learning more about Bayesian statistics?   

1. Under what assumption(s) do sequential and one-step updating of Bayesian posteriors give the same answer?  Demonstrate the equivalence under the appropriate conditions.  (Suggestion: start with two data.)   

1. How should I choose a prior? 

1. What is a "non-informative" prior?  What is a "weakly informative" prior?   

1. What are the common or subtle pitfalls that novices to Bayesian methods fall into?        

1. Why can't I re-use data to update a posterior?
 

<p>[Return to <a href="#Categories">Categories</a>]</p>

## <a name="PDFs">All about pdfs</a>

1. Why do we mostly work with logarithms when dealing with pdfs? 

1. Why do Gaussian distributions appear everywhere? 

1. Why is a normal (Gaussian) distribution so often a good statistical model? 

1. How are the sum of two Gaussian variables distributed?  E.g., if $$X \sim \mathcal{N}(\mu_x, \sigma_x^2)$$ and $$Y \sim \mathcal{N}(\mu_y, \sigma_y^2)$$, then how is $$X + Y$$ distributed?  How about $$X - Y$$?  How about $$aX + bY$$, where $$a$$ and $$b$$ are constants (scalars)? How do you prove these? 

1. How are the sum of two vectors of correlated Gaussian variables distributed? 

1. When does the central limit theorem *not* apply? 


<p>[Return to <a href="#Categories">Categories</a>]</p>

## <a name="Frequentist">Bayesian vs. Frequentist</a>

1. When a weather forecast says there is a 50% chance of rain today, what does that mean to a Bayesian?  What does it mean to a frequentist?

1. Do Bayesians and frequentists disagree about whether Bayes' theorem is valid? 

1. What do Bayesian techniques offer that frequentist statistics does not? 

1. What kinds of problems are ill-suited for Bayesian or frequentist approaches? 
    
1. Doesn't the use of priors make the Bayesian approach completely subjective? 

1. What is the modern view of the conflict (if any) between Bayesian and frequentist statistics? 

<p>[Return to <a href="#Categories">Categories</a>]</p>

## <a name="ParamEst">Parameter estimation</a>


1. What are the assumptions (from a Bayesian perspective) underlying the usual application of the least-square method to fit parameters?   

1. What are some common point estimates for parameters?

1. How is it best to present parameter estimates?

1. How do you identify underfitting / overfitting?

<p>[Return to <a href="#Categories">Categories</a>]</p>

## <a name="Sampling">Sampling</a>

1. When do we need MCMC? 

1. How is MCMC related to the Monte Carlo methods used to solve the Ising model (e.g., in a statistical physics course)? 

1. What is Metropolis-Hastings?  How is it different from Metropolis? 

1. What is Gibbs sampling?  When would you use it? 

1. What is Hamiltonian Monte Carlo? 

1. When should I use Metropolis-Hastings and when should I use Hamiltonian Monte Carlo? 

1. What is the best sampling software for doing MCMC?  E.g., emcee, PyMC3 (or PyMC4?), PyStan, ...


<p>[Return to <a href="#Categories">Categories</a>]</p>

## <a name="Selection">Model selection</a>

1. What is Bayesian model selection?

1. Where in nuclear physics would you apply model selection?

1. What method should I use for calculating the evidence or odds ratios? 

1. How does "PyMultiNest" compute evidences internally?

<p>[Return to <a href="#Categories">Categories</a>]</p>

## <a name="Checking">Model checking</a>
    
1. What is Bayesian model checking?
    
1. What are examples of model checking?

1. How can model checking be used to minimize or validate the influence of priors?
    
<p>[Return to <a href="#Categories">Categories</a>]</p>

## <a name="GPs">Gaussian processes</a>
    
1. Where does the name "Gaussian process" come from?

1. What is the role of the kernel / covariance function?

1. What properties must be fulfilled by a covariance matrix?

1. How can you build a Gaussian emulator?

<p>[Return to <a href="#Categories">Categories</a>]</p>

## <a name="Machine">Bayesian machine learning</a>
   
1. Does machine learning as commonly practiced use Bayesian ideas?
    
1. What is a Bayesian neural network?

1. What is the main challenge when performing Bayesian output predecitions using a neural network?

<p>[Return to <a href="#Categories">Categories</a>]</p>

## <a name="Refs">References, links, etc.</a>

#### Physicist-friendly references:

* R. Trotta, [*Bayes in the sky: Bayesian inference and model selection in cosmology*](https://www.tandfonline.com/doi/abs/10.1080/00107510802066753), Contemp. Phys. **49**, 71 (2008)  [arXiv:0803.4089](https://arxiv.org/abs/0803.4089).
        
* D.S. Sivia and J. Skilling, [*Data Analysis: A Bayesian Tutorial, 2nd edition*]("https://www.amazon.com/Data-Analysis-Bayesian-Devinderjit-Sivia/dp/0198568320/ref=mt_paperback?_encoding=UTF8&me=&qid="), (Oxford University Press, 2006).
    
* P. Gregory,
     [*Bayesian Logical Data Analysis for the Physical Sciences: A Comparative Approach with Mathematica® Support*]("https://www.amazon.com/Bayesian-Logical-Analysis-Physical-Sciences/dp/0521150124/ref=sr_1_1?s=books&ie=UTF8&qid=1538587731&sr=1-1&keywords=gregory+bayesian"), (Cambridge University Press, 2010).
     
* D. MacKay,
     [*Information Theory, Inference, and Learning Algorithms*](http://www.inference.org.uk/mackay/itila/book.html), (Cambridge University Press, 2003).


#### Standard statistics references

* A. Gelman et al., [Bayesian Data Analysis, 3rd edition](https://www.amazon.com/Bayesian-Analysis-Chapman-Statistical-Science/dp/1439840954/ref=sr_1_1?ie=UTF8&qid=1538589213&sr=8-1&keywords=gelman+bayesian+data+analysis) (Chapman and Hall/CRC, 2013).  This is referred to as "BDA-3".

#### Good blogs on statistics and/or machine learning (see also the [list from Andrew Gelman's blog](https://statmodeling.stat.columbia.edu/blogroll/)):

* [*Statistical Modeling, Causal Inference, and Social Science*](https://statmodeling.stat.columbia.edu/) (Andrew Gelman)

* [*While My MCMC Gently Samples*](https://twiecki.io/) (Thomas Wiecki)

* [*Prior Choice Recommendations
*](https://github.com/stan-dev/stan/wiki/Prior-Choice-Recommendations) (stan-dev)

#### Machine learning

* [Hands-On Machine Learning with Scikit-Learn and TensorFlow](https://www.amazon.co.uk/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1491962291) (Aurelien Geron, [github](https://github.com/ageron/handson-ml))

#### Github repositories

* [2019 TALENT course on Learning from Data: Bayesian Methods and Machine Learning](https://github.com/NuclearTalent/Bayes2019) and the associated [website](https://nucleartalent.github.io/Bayes2019/)

<p>[Return to <a href="#Categories">Categories</a>]</p>

<hr>
