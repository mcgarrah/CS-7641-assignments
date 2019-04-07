# Markov Decision Processes

## Environment:

PyCharm Professional running Anaconda Python 3.5 64-bit on Windows 7 Pro 64-bit. The ```requirements.txt``` was
updated to current versions of all libraries for that version of Python.

```
pip install -r requirements.txt
```

Additional ```tensorflow-gpu```, ```theano``` and ```keras``` libraries were included for some experimentation
with deep q-learning (DQL) that did not pan out. CUDA is a requirement if the GPU version of tensorflow is used.

## Output
Output CSVs and images are written to `./output` and `./output/images` respectively. Sub-folders will be created for
each RL algorithm (PI, VI, and Q) as well as one for the final report data.

If these folders do not exist the experiments module will attempt to create them.

##Experiments:

The run_experiment script is used to execute the experiments via:

```
python run_experiment.py --all --verbose
```

Graphing:
---------

The run_experiment script can be use to generate plots via:

```
python run_experiment.py --plot --verbose
```

Since the files output from the experiments follow a common naming scheme this will determine the problem, algorithm,
and parameters as needed and write the output to sub-folders in `./output/images` and `./output/report`.

