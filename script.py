import awswrangler as wr
s3_bucket_name='you_bucket_name'
s3_bucket_file_path='directory_name/'
s3_bucket_path=f"s3://{s3_bucket_name}/{s3_bucket_file_path}"
df=wr.s3.read_csv (path=s3_bucket_path, path_suffix=['.csv'])
print (df)
