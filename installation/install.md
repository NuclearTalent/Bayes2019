Students are encouraged to install python and the required modules
before the start of the school. Please contact the lecturers if you
encounter problems when setting up the environment.


### Installation

Download the repo from github and enter the directory which should have been created on your computer:

    git clone https://github.com/NuclearTalent/Bayes2019.git
    cd Bayes2019

The notebooks that we will be using depend on several scientific python modules (see the list in environment.yml) and require a python3.x installation. 

These python modules and their dependencies are best installed using ``conda`` by creating
a virtual environment:

	conda env create

which reads the environment.yml file in your current directory.

Some packages might not be found in the default conda channels. One
can either specify relevant package channel(s) in the environment.yml
file (as done here), or add them to the default conda channel configuration via, e.g,

	conda config --append channels conda-forge

Once the virtual environment has been created it can be activated:

    conda activate talent-env

To deactivate the virtual environment:

    conda deactivate

Note that earlier versions of conda used 'source' instead of 'conda'
to activate environments. If you have an earlier version of conda you
might have to do

    conda update conda

Note that there are also other options ('venv', 'pipenv') for creating virtual
environments that includes the python version and packages that we will be using.

Once the environment is set up and activated, you are encouraged to enter the intro directory and start the jupyter notebook:

    cd intro
    jupyter notebook bayesTALENT_intro.ipynb
