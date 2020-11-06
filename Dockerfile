#FROM continuumio/miniconda3
#ADD environment.yml
#RUN conda env create --file environment.yml
#ADD resulting.py /
#ADD latimes-state-totals.csv /
#ADD cdph-race-ethnicity.csv /
#CMD ["bokeh","serve","--show", "resulting.py"]


FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
#SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]
RUN conda env create --file environment.yml

# The code to run when container is started:
COPY run.py .
ENTRYPOINT ["conda", "run", "-n", "myenv", "python", "run.py"]
