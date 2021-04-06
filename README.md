# Using DVC with S3

With the release of DVC 2.0 in Mar 2021, I am updating this branch. DVC 2.0 provides greater functionality especially in terms of Experiment Management. At this time of writing, the below codes were used with DVC version 2.0.17.

The `pipeline` branch is where I used `dvc run` commands to create the DVC pipeline. The `dvc.yaml` and `dvc.lock` files contain the stages in the pipeline and the corresponding MD5 hashes of the dependencies and outputs of the particular stage.

I had referenced the official DVC tutorial and made changes to the scripts such that the data is found in raw, interim and processed subfolders. There were changes made to the DVC commands below. 

```
dvc run -n prepare \
        -p prepare.seed,prepare.split \
        -d src/prepare.py -d data/raw/data.xml \
        -o data/interim/train.tsv -o data/interim/test.tsv \
        python src/prepare.py data/raw/data.xml

dvc run -n featurize \
        -p featurize.max_features,featurize.ngrams \
        -d src/featurization.py -d data/interim/train.tsv -d data/interim/test.tsv \
        -o data/processed/train.pkl -o data/processed/test.pkl \
        python src/featurization.py data/interim data/processed

dvc run -n train \
        -p train.seed,train.n_est,train.min_split \
        -d src/train.py -d data/processed/train.pkl -d data/processed/test.pkl \
        -o model.pkl \
        python src/train.py data/processed model.pkl

git add dvc.yaml dvc.lock .gitignore
git commit -m "1st 3 stages of pipeline"
git push
dvc push

dvc run -n evaluate \
        -d src/evaluate.py -d model.pkl -d data/processed/train.pkl -d data/processed/test.pkl \
        -M scores.json \
        --plots-no-cache prc.json \
        --plots-no-cache roc.json \
        python src/evaluate.py model.pkl data/processed scores.json prc.json roc.json

# View tracked metrics.
dvc metrics show
# View plots. First, have to specify which arrays to use as the plot axes.
dvc plots modify prc.json -x recall -y precision
dvc plots modify roc.json -x fpr -y tpr
dvc plots show

git add dvc.yaml dvc.lock
git commit -m "4th stage of pipeline"
git add scores.json prc.json roc.json
git commit -m "Metrics for 4th stage"
git add plots.html
git commit -m "Plots for 4th stage"
git push
# NO NEED dvc push


# 2nd experiment
# Amend params.yaml file. Max_features change from 500 to 1500. Ngrams change from 1 to 2.
dvc repro
# dvc repro reads from dvc.yaml, and uses dvc.lock which contains the MD5 hashes to determine what exactly needs to be run.

# View difference in parameters or metrics between workspace and last commit.
dvc params diff
dvc metrics diff
dvc plots diff

# Push the changes. No change in the dvc.yaml file.
git add params.yaml dvc.lock scores.json prc.json roc.json plots.html
git commit -m "Max features 1500 and bigrams"
git push
dvc push


# 3rd experiment
dvc exp run --set-param featurize.max_features=3000

dvc exp diff
# OPTIONAL View difference in parameters or metrics between workspace and last commit.
dvc params diff
dvc metrics diff
dvc plots diff

# Push the changes.
git add params.yaml dvc.lock scores.json prc.json roc.json plots.html
git commit -m "Max features 3000 and remain as bigrams"
git push
dvc push


# 4th experiment contains 5 sub-experiments being queued.
dvc exp run --queue -S train.min_split=8
dvc exp run --queue -S train.min_split=64
dvc exp run --queue -S train.min_split=2 -S train.n_est=100
dvc exp run --queue -S train.min_split=8 -S train.n_est=100
dvc exp run --queue -S train.min_split=64 -S train.n_est=100

# Run queued experiments in parallel.
dvc exp run --run-all --jobs 2

# Compare experiments. This only shows experiments since the last commit.
dvc exp show --no-timestamp --include-params train.n_est,train.min_split --no-pager

# Apply best experiment to the workspace. The experiment will be made persistent. 
dvc exp apply exp-e1dec

# OPTIONAL View difference in parameters or metrics between workspace and last commit.
dvc params diff
dvc metrics diff
dvc plots diff

# Push the changes.
git add params.yaml dvc.lock scores.json prc.json roc.json plots.html
git commit -m "Best experiment"
git push
dvc push

# After applying the best experiment, the experiments table is cleaned up.
dvc exp show --no-timestamp --include-params train.n_est,train.min_split --no-pager
# View experiments from the previous n commits.
dvc exp show -n 2 --no-timestamp --include-params train.n_est,train.min_split  --no-pager
dvc exp show -n 4 --no-timestamp --include-params train.n_est,train.min_split  --no-pager


# Removing references to old experiments.
dvc exp gc --workspace
dvc exp show -n 4 --no-timestamp --include-params train.n_est,train.min_split  --no-pager
```

Summary of 4 experiments
![image](https://user-images.githubusercontent.com/51873343/113694735-b78afc80-9702-11eb-929c-ba8cb3f9ac6a.png)

S3 bucket shows the additional content related to the experiments.

![image](https://user-images.githubusercontent.com/51873343/113695321-4e57b900-9703-11eb-91ab-284cd3cf7c1b.png)
