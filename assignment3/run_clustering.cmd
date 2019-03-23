REM @ECHO OFF

REM Replace 'X' below with the optimal values found. Starting with '2'
REM If you want to first generate data and updated datasets, remove the "--skiprerun" flags below

set logs=.\logs
IF exist %logs% ( echo %logs% exists ) ELSE ( mkdir %logs% && echo %logs% created)

REM https://support.microsoft.com/en-us/help/110930/redirecting-error-messages-from-command-prompt-stderr-stdout

REM Run the cluster algorithms on the datasets and describe what you see.
python run_experiment.py --benchmark --threads -1 --seed 0 --plot > logs/00-benchmark-all-datasets.log 2>&1

REM Apply dimensionality reduction algorithms to datasets and describe what you see.
python run_experiment.py --ica --pca --rf --rp --threads -1 --seed 0 --plot > logs/01-dimreduce-all-datasets.log 2>&1
REM ICA took 28 minutes and totals took from about 1pm until 4:30pm so about 3 to 3.5 hours total time for both datasets

REM Backup the experiments for later analysis - we need the graphs before the diminensional reduction
set dtstr=%date:~10,4%%date:~7,2%%date:~4,2%T%time:~0,2%%time:~3,2%%time:~6,2%
XCOPY /E /C /I output output-%dtstr%
IF exist output-%dtstr% ( echo Backup made of output folder ) ELSE ( echo ERROR )

REM Get the --dim values for each from ./output/images review
REM STATLOG
python run_experiment.py --ica --dataset1 --dim 20  --skiprerun --verbose --seed 0 --threads -1 --plot > logs/02-ica-dataset1-clustering.log 2>&1
python run_experiment.py --pca --dataset1 --dim 18  --skiprerun --verbose --seed 0 --threads -1 --plot > logs/02-pca-dataset1-clustering.log 2>&1
python run_experiment.py --rp  --dataset1 --dim 25  --skiprerun --verbose --seed 0 --threads -1 --plot > logs/02-rp-dataset1-clustering.log 2>&1
python run_experiment.py --rf  --dataset1 --dim 17  --skiprerun --verbose --seed 0 --threads -1 --plot > logs/02-rf-dataset1-clustering.log 2>&1

REM HRTU
python run_experiment.py --ica --dataset2 --dim 8 --skiprerun --verbose --seed 0 --threads -1 --plot > logs/02-ica-dataset2-clustering.log 2>&1
python run_experiment.py --pca --dataset2 --dim 10 --skiprerun --verbose --seed 0 --threads -1 --plot > logs/02-pca-dataset2-clustering.log 2>&1
python run_experiment.py --rp  --dataset2 --dim 30 --skiprerun --verbose --seed 0 --threads -1 --plot > logs/02-rp-dataset2-clustering.log 2>&1
python run_experiment.py --rf  --dataset2 --dim 7 --skiprerun --verbose --seed 0 --threads -1 --plot > logs/02-rf-dataset2-clustering.log 2>&1

python run_experiment.py --seed 0 --plot > logs/02-plot-all-clustering.log 2>&1

REM (base) C:\Users\mcgarrah\CS-7641-assignments\assignment3>python run_experiment.py --ica --dataset2 --dim 2 --skiprerun --verbose --seed 0 --threads -1 > ica-dataset2-clustering.log