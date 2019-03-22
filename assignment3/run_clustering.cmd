REM @ECHO OFF

REM Replace 'X' below with the optimal values found. Starting with '2'
REM If you want to first generate data and updated datasets, remove the "--skiprerun" flags below

IF exist logs ( echo logs exists ) ELSE ( mkdir logs && echo logs created)

REM https://support.microsoft.com/en-us/help/110930/redirecting-error-messages-from-command-prompt-stderr-stdout

python run_experiment.py --ica --statlog --dim 2  --skiprerun --verbose --seed 0 --threads -1 > logs/ica-statlog-clustering.log 2>&1
python run_experiment.py --pca --statlog --dim 2  --skiprerun --verbose --seed 0 --threads -1 > logs/pca-statlog-clustering.log 2>&1
python run_experiment.py --rp  --statlog --dim 2  --skiprerun --verbose --seed 0 --threads -1 > logs/rp-statlog-clustering.log 2>&1
python run_experiment.py --rf  --statlog --dim 2  --skiprerun --verbose --seed 0 --threads -1 > logs/rf-statlog-clustering.log 2>&1
REM python run_experiment.py --svd --statlog --dim X  --skiprerun --verbose --seed 0 --threads -1 > logs/svd-statlog-clustering.log 2>&1

python run_experiment.py --ica --htru2   --dim 2  --skiprerun --verbose --seed 0 --threads -1 > logs/ica-htru2-clustering.log 2>&1
python run_experiment.py --pca --htru2   --dim 2  --skiprerun --verbose --seed 0 --threads -1 > logs/pca-htru2-clustering.log 2>&1
python run_experiment.py --rp  --htru2   --dim 2  --skiprerun --verbose --seed 0 --threads -1 > logs/rp-htru2-clustering.log 2>&1
python run_experiment.py --rf  --htru2   --dim 2  --skiprerun --verbose --seed 0 --threads -1 > logs/rf-htru2-clustering.log 2>&1
REM python run_experiment.py --svd --htru2   --dim X  --skiprerun --verbose --seed 0 --threads -1 > svd-htru2-clustering.log 2>&1

python run_experiment.py --ica --titanic --dim 2 --skiprerun --verbose --seed 0 --threads -1 > logs/ica-titanic-clustering.log 2>&1
python run_experiment.py --pca --titanic --dim 2 --skiprerun --verbose --seed 0 --threads -1 > logs/pca-titanic-clustering.log 2>&1
python run_experiment.py --rp  --titanic --dim 2 --skiprerun --verbose --seed 0 --threads -1 > logs/rp-titanic-clustering.log 2>&1
python run_experiment.py --rf  --titanic --dim 2 --skiprerun --verbose --seed 0 --threads -1 > logs/rf-titanic-clustering.log 2>&1

python run_experiment.py --ica --pendigit --dim 2 --skiprerun --verbose --seed 0 --threads -1 > logs/ica-pendigit-clustering.log 2>&1
python run_experiment.py --pca --pendigit --dim 2 --skiprerun --verbose --seed 0 --threads -1 > logs/pca-pendigit-clustering.log 2>&1
python run_experiment.py --rp  --pendigit --dim 2 --skiprerun --verbose --seed 0 --threads -1 > logs/rp-pendigit-clustering.log 2>&1
python run_experiment.py --rf  --pendigit --dim 2 --skiprerun --verbose --seed 0 --threads -1 > logs/rf-pendigit-clustering.log 2>&1

python run_experiment.py --seed 0 --plot > logs/plot-all-clustering.log 2>&1

REM (base) C:\Users\mcgarrah\CS-7641-assignments\assignment3>python run_experiment.py --ica --titanic --dim 2 --skiprerun --verbose --seed 0 --threads -1 > ica-titanic-clustering.log