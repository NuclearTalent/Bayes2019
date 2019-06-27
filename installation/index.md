<p align="right"><a href="https://nucleartalent.github.io/Bayes2019/">Return to home</a></p> 

## Installation instructions

### Setup python environment: 

See the [installation instructions](install.md).

### Update conda python environment 

New python packages can simply be installed with `pip` or `conda`. However, in order to reproduce the environment for someone else (including all dependencies), it is better to include them in the `environment.yml` file. 

Suppose that you already have a working environment, but that you receive an updated environment file. You can then update your outdated conda environment by the following sequence (where 'path/to/environment.yml' is the path to the directory that contains the environment file, which in our case is the root of your copy of the course github repository)

    conda deactivate
    conda env update -f path/to/environment.yml
    conda activate talent-env
    
Test your installation by opening a jupyter notebook, or a python session, and check that you can import the new modules without any error messages. E.g., having added `GPy`, `pymc3`, and `pymultinest`, to your environment you should try

    >>> import GPy
    >>> import pymc3
    >>> import pymultinest


### Install multinest

In order to use `pymultinest`within python you need to have a working version of `multinest`installed and the path to its library setup correctly. The following set of commands should work

    git clone https://github.com/JohannesBuchner/MultiNest
    cd MultiNest/build
    cmake ..
    make
    sudo make install
    
if you have `cmake` and fortran compilers on your system. In case the import of the module still fails (with an error message about not finding the multinest library file) you can try setting the library path. With the bash shell you can do

    export LD_LIBRARY_PATH="/path/to/lib:$LD_LIBRARY_PATH"
    
where `/path/to/lib` is the path to the `lib` directory of your Multinest build that should contain the library file. You might consider putting this command in your `.bashrc` file so that it is done automatically.


You can also read the full set of instructions at the PyMultinest [installation guide](http://johannesbuchner.github.io/PyMultiNest/install.html). 
