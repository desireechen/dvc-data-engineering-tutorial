# Using DVC with S3

This was created as a tutorial on how DVC has been integrated into GitLab projects. DVC remote storage `.dvc_cache` has been configured to be in S3.

The main branch is how it starts out after the raw dataset has been uploaded into S3.  

This is what is in S3 bucket upon uploading the raw dataset. 

![image](https://user-images.githubusercontent.com/51873343/108140239-a3605100-70fc-11eb-9ced-ea6290ab3e07.png)

The `.dvc` file corresponding to the raw dataset can be found in the `data/raw` folder.

Do a `dvc pull` to get the `.csv` raw dataset in your local `data/raw` folder. There will also be a folder `.dvc/cache` in your local machine containing the hash value of the dataset.

### Getting the data used in a particular branch

1. Clone the repository. <br>
2. `git checkout <branch_name>` <br>
3. `dvc pull` <br>
