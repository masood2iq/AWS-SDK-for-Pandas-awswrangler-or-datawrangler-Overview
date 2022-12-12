# AWS_SDK_for_Pandas_(awswrangler_or_datawrangler)_Overview

## Description
This is an overview of the AWS SDK for pandas (awswrangler) which is an open-source python library that makes it easier to work with data from AWS services.

## Overview
[AWS Data Wrangler](https://aws-sdk-pandas.readthedocs.io/en/stable/index.html) is an open-source Python library built on top of [Pandas](https://github.com/pandas-dev/pandas), [Apache Arrow](https://github.com/apache/arrow), and [Boto3](https://github.com/boto/boto3), it offers abstracted functions to execute usual ETL tasks like loading/unloading data from Data Lakes, Data Warehouses, and Databases using python.
AWS [datawrangler](https://aws-sdk-pandas.readthedocs.io/en/stable/index.html#) is easily integrated with AWS services like [AWS S3, AWS Glue, Amazon Athena](https://github.com/masood2iq/AWS_Athena_Glue_S3_CloudFormation_Deployment_AWSConsole), AWS DynamoDB, AWS CloudWatch, AWS Redshift, Amazon Timestream, AWS EMR, etc.
Working with data datawrangler support reading and writing Excel, JSON, CSV, and Parquet from S3. Interact with data and metadata through AWS Glue and run SQL queries on Amazon Athena.

**Note:** Before working with AWS [datawrangler](https://aws-sdk-pandas.readthedocs.io/en/stable/index.html) you need to install and configure your [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) account on your Linux machine.

Now, before installing **[datawrangler](https://aws-sdk-pandas.readthedocs.io/en/stable/index.html)**, we need to install the **python3** on our Linux machine, which can be done with commands

``` sh
$ apt update
```  

``` sh
$ apt install -y python3
```

After installation of **python3**, we need to install the python package **pip**, which can be done with commands

``` sh
$ apt install python3-pip
```

``` sh
$ pip3 install --upgrade pip
```

``` sh
$ apt install -y python3-venv
```

![](./images/image10.png)

  
# To create a virtual environment for python 3, we can do it in two ways as
  
----
### <u>**WAY - 1**</u>
----
Create a virtual environment, which can be done with commands.

``` sh
$ python3 -m venv my_env_project
```

![](./images/image7.png)


The above command creates a directory named `my_env_project` in the current directory, which contains pip, interpreter, scripts, and libraries, view as

``` sh
$ ls my_env_project/
```

![](./images/image24.png)


You can now `activate the virtual environment`, with the command

``` sh
$ source my_env_project/bin/activate
```

![](./images/image1.png)


Command prompt would change to your environment and will look as shown

``` sh
(my_env_project) ubuntu@DESKTOP-I4BBP24:~$
```

![](./images/image20.png)


Now, we install the `awswrangler` package into our `virtual environment` as

``` sh
(my_env_project)$ pip install awswrangler
```

![](./images/image16.png)


Now, if you didn’t configured AWS CLI, configure as

``` sh
(my_env_project)$ aws configure
```

![](./images/image25.png)


Run python command inside `virtual environment` to open the interpreter

``` sh
(my_env_project)$ python
```

![](./images/image18.png)


Every time you install a new package inside your `virtual environment`, you should be able to import it into your project.
Now let’s test `awswrangler` with `S3 bucket`.

``` sh
(my_env_project) ubuntu@DESKTOP-I4BBP24:~/my_env_project$ python
>>> import awswrangler as wr
>>> s3_bucket_name='you_bucket_name'
>>> s3_bucket_file_path='directory_name/'
>>> s3_bucket_path=f"s3://{s3_bucket_name}/{s3_bucket_file_path}"
>>> df=wr.s3.read_csv (path=s3_bucket_path, path_suffix=['.csv'])
>>> print (df)
```

![](./images/image13.png)


To exit from the interpreter, type

``` sh
>>> quit()
```

We can also create a python script and run from inside python 3 `virtual environment` as

``` sh
(my_env_project) ubuntu@ubuntu:~$ vim script.py
```

Copy and paste the given code inside the script file

``` py
import awswrangler as wr
s3_bucket_name='you_bucket_name'
s3_bucket_file_path='directory_name/'
s3_bucket_path=f"s3://{s3_bucket_name}/{s3_bucket_file_path}"
df=wr.s3.read_csv (path=s3_bucket_path, path_suffix=['.csv'])
print (df)
```

![](./images/image6.png)


To execute the script, run command

``` sh
(my_env_project) ubuntu@ubuntu:~$ python script.py
```

![](./images/image23.png)


To exit from `virtual environment` use `exit` or `Ctrl+d` command. To delete a `virtual environment` run the following command

``` sh
(my_env_project) ubuntu@ubuntu:~$ deactivate
```

![](./images/image14.png)


The above command won't remove `my_env_project` directory, simply use `rm` command to delete it.
  
----
### <u>**WAY - 2**</u>
----
Create a directory and go into it to create `virtual environment` as

``` sh
$ mkdir jupyter_notebook
```

``` sh
$ ls jupyter_notebook

$ cd jupyter_notebook
```

![](./images/image9.png)


Now, create a python `virtual environment` named `jupypter_notebook`

``` sh
$ virtualenv jupyter_notebook
```

![](./images/image22.png)


To `activate` and get inside that `virtual environment`

``` sh
$ source jupyter_notebook/bin/activate
```

![](./images/image4.png)


Install `Jupyter` inside the `virtual environment`

``` sh
(jupyter_notebook) ubuntu@ubuntu:~/jupyter_notebook$ pip3 install jupyter
```

![](./images/image3.png)


Create a `kernel` that can be used to run `python` commands inside the `virtual environment` of `jupyter notebook`.

``` sh
(jupyter_notebook) ubuntu@ubuntu:~/jupyter_notebook$ ipython kernel install --user --name=python-env
```

![](./images/image21.png)


You can launch its web interface from the terminal as

``` sh
(jupyter_notebook) ubuntu@ubuntu:~/jupyter_notebook$ jupyter notebook --allow-root
```

![](./images/image8.png)


You get the link to open it in your browser, click on right side, `New` drop down menu and select your `python_env`.

![](./images/image19.png)


Install `awswrangler` with command given in your `python_env` virtual environment.

```
pip install awswrangler
```

![](./images/image17.png)


Run the following code to test the `awswrangler` with your `S3 Bucket` to get the data from `.csv` file.

``` py
import awswrangler as wr
s3_bucket_name='you_bucket_name'
s3_bucket_file_path='directory_name/'
s3_bucket_path=f"s3://{s3_bucket_name}/{s3_bucket_file_path}"
df=wr.s3.read_csv (path=s3_bucket_path, path_suffix=['.csv'])
print (df)
```

![](./images/image15.png)


After you are done with the project, exit from `Jupyter` from the browser and no longer need the `kernel` you can uninstall it with the command.

``` sh
(jupyter_notebook) ubuntu@ubuntu:~/jupyter_notebook$ jupyter-kernelspec uninstall python-env
```
 
![](./images/image2.png)


To exit from `virtual environment`

``` sh
(jupyter_notebook) ubuntu@ubuntu:~/jupyter_notebook$ deactivate
```

![](./images/image5.png)


To delete the `virtual environment`

``` sh
virtualenv --clear /home/ubuntu/jupyter-notebook/
```

![](./images/image11.png)
