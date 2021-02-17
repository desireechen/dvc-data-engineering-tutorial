# Using DVC with S3

The `dvc` branch is where I had used various `DVC` commands to add and commit dataset changes to both my local DVC cache and the remote DVC storage.

`src` folder contains scripts that create the interim and processed datasets from the raw dataset that was uploaded.

```
git add src/clean.py src/split.py
git commit -m "Added scripts"
git push
```

If the file is already under DVC's control, use `dvc commit`. If the file is not yet under DVC's control and is now going under DVC's control, use `dvc add`. 

After making a change to the raw dataset (which is already under DVC's control), do `dvc commit`. The MD5 hash in the `.dvc` file woould change to one starting with 23 (previously in the main branch, it was starting with 13). Push the change to Git and S3.

```
git add data/raw/resale-prices.csv.dvc data/raw/.gitignore
git commit -m "Amended contents in raw folder"
git push
dvc push
```

S3 bucket shows the additional content related to the raw dataset.

![image](https://user-images.githubusercontent.com/51873343/108139288-beca5c80-70fa-11eb-8859-088c6eddcac3.png)

Create the interim (removed duplicates in raw dataset) and processed datasets (split interim dataset into train and test).

```
python src/clean.py
python src/split.py
```

Push the changes to both Git and S3.

```
dvc add data/interim/resale-prices-removed-duplicates.csv
git add data/interim/resale-prices-removed-duplicates.csv.dvc data/interim/.gitignore
git commit -m "Removed duplicates"
dvc add data/processed/*
git add data/processed/resale-prices-train.csv.dvc data/processed/resale-prices-test.csv.dvc data/processed/.gitignore
git commit -m "Split data into train and test"
git push
dvc push
```

S3 bucket shows the additional content related to the interim and processed datasets.

![image](https://user-images.githubusercontent.com/51873343/108139357-e6b9c000-70fa-11eb-9945-3a87f35f2a14.png)
