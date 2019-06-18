## Installation instructions

### Setup python environment: 

See the [installation instructions](install.md).

### Update conda python environment 

New python packages can simply be installed with `pip` or `conda`. However, in order to reproduce the environment for someone else (including all dependencies), it is better to include them in the `environment.yml` file. 

Suppose that you already have a working environment, but that you receive an updated environment file. You can then update your outdated conda environment by the following sequence (where 'path/to/environment.yml' is the path to the directory that contains the environment file, which in our case is the root of your copy of the course github repository)

    conda deactivate
    conda env update -f path/to/environment.yml
    conda activate talent-env


### Install multinest

In order to use `pymultinest`within python you need to have a working version of `multinest`installed and the path to its library setup correctly. The following set of commands should work

    git clone https://github.com/JohannesBuchner/MultiNest
    cd MultiNest/build
    cmake ..
    make
    sudo make install
    
if you have `cmake` and fortran compilers on your system. You can also read the full set of instructions at the PyMultinest [installation guide](http://johannesbuchner.github.io/PyMultiNest/install.html). 
