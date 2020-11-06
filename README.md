# California Coronavirus Data Visualizations

## Overview
This repository contains data related to the coronavirus epidemic in the state of California, and the script ```resulting.py``` to carry out visualizations on some of the data.

## Installation

First, start by closing the repository:
```
git clone https://github.com/sharmasharad795/california-coronavirus-data.git
```
It is recommended to use a virtualenv for your development

- Create a new conda environment of your choice of name (bokvisuals here is the name of the environment)
```
conda create --name bokvisuals 
```
- Activate the environment
```
conda activate bokvisuals
```
- Install the dependencies to run the project
```
conda install numpy pandas jupyter bokeh
```

## Invocation

We can now run the visualization script in the following way:

```
bokeh serve --show resulting.py
```
To stop the server , use ```Ctrl + C```

Once the scripts have been run, the conda virutalenv can be closed using the command ```conda deactivate```







