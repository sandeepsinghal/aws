import boto3

#s3 = boto3.resource('s3', region_name='us-west-2')

#for bucket in s3.buckets.all():
#    print(bucket.name)


s3 = boto3.client('s3')

response = s3.list_buckets()

for bucket in response['Buckets']:
    print(f"{bucket['Name']} - {bucket['CreationDate']}")
