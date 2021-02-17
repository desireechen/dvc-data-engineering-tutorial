# Using DVC with S3

This was created as a tutorial on how DVC has been integrated into GitLab projects. DVC remote storage `.dvc_cache` has been configured to be in S3.

### Summary of branches

The `before-upload` branch shows how the project starts off initially before the raw dataset is uploaded into S3.

This `main` branch is how it starts out after the raw dataset has been uploaded into S3.

The `with-scripts` branch shows the addition of scripts used subsequently to create interim and processed datasets from the raw dataset that was uploaded.

The `dvc` and `pipeline` branches are spawned from the `with-scripts` branch. The `dvc` branch shows the use of `dvc add` or `dvc commit` to make changes to both my local DVC cache and the remote DVC storage. The `pipeline` branch shows the use of `dvc run` to create the DVC pipeline.

This is what is in S3 bucket upon uploading the raw dataset. 

![image](https://user-images.githubusercontent.com/51873343/108140239-a3605100-70fc-11eb-9ced-ea6290ab3e07.png)

The `.dvc` file corresponding to the raw dataset can be found in the `data/raw` folder.

Do a `dvc pull` to get the `.csv` raw dataset in your local `data/raw` folder. There will also be a folder `.dvc/cache` in your local machine containing the hash value of the dataset.

### Getting the data used in a particular branch

1. Clone the repository. <br>
2. `git checkout <branch_name>` <br>
3. `dvc pull` <br>
