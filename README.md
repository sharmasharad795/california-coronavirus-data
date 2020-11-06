# California Coronavirus Data Visualizations

## Overview
This repository contains data related to the coronavirus epidemic in the state of California, and the script ```resulting.py``` to carry out visualizations on some of the data.

## Installation
First, start by closing the repository:
```
git clone https://github.com/sharmasharad795/california-coronavirus-data.git
```
It is recommended to use a virtualenv for your development
- Install the virualenv
```
pip install virtualenv
```
- Create the environment of your choice of name (env here is the name of the environment)
```
python -m venv env 
```
- Activate the environment
```
source env/bin/activate
```
- Install the dependencies to run the project
```
pip install -r requirements.txt
```

## Invocation

We can now run the visualization script in the following way:

```
bokeh serve --show resulting.py
```
To stop the server , use ```Ctrl + C```

## Docker
- First , get docker on your local system by downloading from this link : https://docs.docker.com/get-docker/

- Inside your cloned repository , perform ```vi Dockerfile``` to create a Dockerfile.

- The Dockerfile should be filled as follows:

```
FROM python:3.7
WORKDIR /visual
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD resulting.py .
ADD latimes-state-totals.csv .
ADD cdph-race-ethnicity.csv .
CMD ["bokeh","serve","--show", "resulting.py"]
```
- Create a Docker Image with the help of ```docker build --tag bokehvisual .``` where ```bokehvisual``` is the name of the image

- Display the images, including the recently created one using ```docker images```

- Now, run ```docker run -p 5006:5006 -it bokehvisual``` to see the visualizations.

- Launch ``` http://localhost:5006/resulting``` from your preferred browser.

- Once done, use ```Ctrl + C```

Once the scripts have been run, the ```virutalenv``` can be closed using the command ```deactivate```



