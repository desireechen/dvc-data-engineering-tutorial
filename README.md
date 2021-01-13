# Using DVC with S3

The `pipeline` branch is where I used `dvc run` commands to create the DVC pipeline. The `dvc.yaml` and `dvc.lock` files contain the stages in the pipeline and the corresponding MD5 hashes of the dependencies and outputs of the particular stage. <br>

`dvc run -n clean \
        -d src/clean.py -d data/raw/resale-prices.csv \
        -o data/interim/resale-prices-removed-duplicates.csv \
        python src/clean.py` <br>
        
`dvc run -n split \
        -d src/split.py -d data/interim/resale-prices-removed-duplicates.csv \
        -o data/processed/resale-prices-train.csv -o data/processed/resale-prices-test.csv \
        python src/split.py` <br>
        
Push the changes to both Git and S3. <br>
`dvc commit` <br>
`git add data/interim/.gitignore data/processed/.gitignore dvc.lock dvc.yaml` <br>
`git commit -m "Pipeline to clean and split data"` <br>
`git push` <br>
`dvc push` <br>

S3 bucket shows the additional content related to the interim and processed datasets.

![image](https://user-images.githubusercontent.com/51873343/104393811-4a8f1d00-5580-11eb-99f1-5c70cc4ce94c.png)
