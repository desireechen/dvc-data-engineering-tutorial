# Using DVC with S3

The `dvc` branch is where I had used various `DVC` commands to add and commit dataset changes to both my local DVC cache and the remote DVC storage.

`src` folder contains scripts that create the interim and processed datasets from the raw dataset that was uploaded.

`git add src/clean.py src/split.py`
`git commit -m "Added scripts"`
`git push`

If the file is already under DVC's control, use `dvc commit`. If the file is not yet under DVC's control and is now going under DVC's control, use `dvc add`. 

After making a change to the raw dataset (which is already under DVC's control), do `dvc commit`. The MD5 hash in the `.dvc` file woould change to one starting with 23 (previously in the main branch, it was starting with 13). Push the change to Git and S3. <br>
`git add data/raw/resale-prices.csv.dvc data/raw/.gitignore` <br>
`git commit -m "Amended contents in raw folder"` <br>
`git push` <br>
`dvc push` <br>

S3 bucket shows the additional content related to the raw dataset.

![image](https://user-images.githubusercontent.com/51873343/104392993-4feb6800-557e-11eb-8455-72ed7b93d4e6.png)

Create the interim (removed duplicates in raw dataset) and processed datasets (split interim dataset into train and test). <br>
`python src/clean.py` <br>
`python src/split.py` <br>

Push the changes to both Git and S3.
`dvc add data/interim/resale-prices-removed-duplicates.csv` <br>
`git add data/interim/resale-prices-removed-duplicates.csv.dvc data/interim/.gitignore` <br>
`git commit -m "Removed duplicates"` <br>
`dvc add data/processed/*` <br>
`git add data/processed/resale-prices-train.csv.dvc data/processed/resale-prices-test.csv.dvc data/processed/.gitignore` <br>
`git commit -m "Split data into train and test"` <br>
`git push` <br>
`dvc push` <br>

S3 bucket shows the additional content related to the interim and processed datasets.

![image](https://user-images.githubusercontent.com/51873343/104393266-fdf71200-557e-11eb-8070-2e35abc1c540.png)
