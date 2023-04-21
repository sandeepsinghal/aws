import boto3

region_name = 'us-west-2'
s3 = boto3.resource('s3', region_name=region_name)

bucket_name = 'chatgpt'

s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
    'LocationConstraint': region_name
})
