REM @ECHO OFF

REM Replace 'X' below with the optimal values found. Starting with '2'
REM If you want to first generate data and updated datasets, remove the "--skiprerun" flags below

set logs=.\logs
IF exist %logs% ( echo %logs% exists ) ELSE ( mkdir %logs% && echo %logs% created)

REM https://support.microsoft.com/en-us/help/110930/redirecting-error-messages-from-command-prompt-stderr-stdout

python run_experiment.py --ica --dataset1 --dim 2  --skiprerun --verbose --seed 0 --threads -1 > logs/ica-dataset1-clustering.log 2>&1
python run_experiment.py --pca --dataset1 --dim 2  --skiprerun --verbose --seed 0 --threads -1 > logs/pca-dataset1-clustering.log 2>&1
python run_experiment.py --rp  --dataset1 --dim 2  --skiprerun --verbose --seed 0 --threads -1 > logs/rp-dataset1-clustering.log 2>&1
python run_experiment.py --rf  --dataset1 --dim 2  --skiprerun --verbose --seed 0 --threads -1 > logs/rf-dataset1-clustering.log 2>&1

python run_experiment.py --ica --dataset2 --dim 2 --skiprerun --verbose --seed 0 --threads -1 > logs/ica-dataset2-clustering.log 2>&1
python run_experiment.py --pca --dataset2 --dim 2 --skiprerun --verbose --seed 0 --threads -1 > logs/pca-dataset2-clustering.log 2>&1
python run_experiment.py --rp  --dataset2 --dim 2 --skiprerun --verbose --seed 0 --threads -1 > logs/rp-dataset2-clustering.log 2>&1
python run_experiment.py --rf  --dataset2 --dim 2 --skiprerun --verbose --seed 0 --threads -1 > logs/rf-dataset2-clustering.log 2>&1

python run_experiment.py --seed 0 --plot > logs/plot-all-clustering.log 2>&1

REM (base) C:\Users\mcgarrah\CS-7641-assignments\assignment3>python run_experiment.py --ica --dataset2 --dim 2 --skiprerun --verbose --seed 0 --threads -1 > ica-dataset2-clustering.log