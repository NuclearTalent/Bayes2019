## Installation instructions

### Setup python environment: 

See the [installation instructions](install.md)

### Update conda python environment 

If we decide to add new python packages to our environment we can simply install them with 'pip' or conda. But in order to reproduce the environment for someone else (including all dependencies), it is better to include them in the 'environment.yml' file. Given an updated environment file you can update your conda environment by the following sequence (where 'path/to/environment.yml' is the path to the directory that contains the environment file, which is the root of your copy of the course github repository)

    conda deactivate
    conda env update -f path/to/environment.yml
    conda activate talent-env


### Install multinest

In order to use `pymultinest`within python you need to have a working version of `multinest`installed and the paths to the libraries setup correctly. The following set of commands should wotk

    git clone https://github.com/JohannesBuchner/MultiNest
    cd MultiNest/build
    cmake ..
    make
    sudo make install
    
if you have `cmake` and fortran compilers on your system. You can also read the full set of instructions at the PyMultinest [installation guide](http://johannesbuchner.github.io/PyMultiNest/install.html). 
