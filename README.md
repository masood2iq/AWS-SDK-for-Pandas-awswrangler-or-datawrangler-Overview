# AWS_SDK_for_Pandas_(awswrangler_or_datawrangler)_Overview

## Description
This is an overview of the AWS SDK for pandas (awswrangler) which is an open-source python library that makes it easier to work with data from AWS services.

## Overview
<p>
[AWS Data Wrangler] is an open-source Python library built on top of [Pandas], [Apache Arrow], and [Boto3], it offers abstracted functions to execute usual ETL tasks like loading/unloading data from Data Lakes, Data Warehouses, and Databases using python.
AWS [datawrangler] is easily integrated with AWS services like {AWS S3, AWS Glue, Amazon Athena, AWS DynamoDB, AWS CloudWatch, AWS Redshift, Amazon Timestream, AWS EMR, etc}.
Working with data datawrangler support reading and writing Excel, JSON, CSV, and Parquet from S3. Interact with data and metadata through AWS Glue and run SQL queries on Amazon Athena.
</p>

**[Note:]** Before working with AWS [datawrangler] you need to install and configure your [AWS CLI] account on your Linux for which you can use given link  


Now, before installing **[datawrangler]**, we need to install the [python3] on our Linux machine, which can be done as  

```sh
$ apt update
```  

```sh
$ apt install -y python3
```

After installation of [python3], we need to install the python package [pip], which can be done as

```sh
apt install python3-pip
```

```sh
pip3 install --upgrade pip
```
