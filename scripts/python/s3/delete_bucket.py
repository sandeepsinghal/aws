import boto3

s3 = boto3.resource('s3', region_name='us-west-2')

bucket_name = 'sandeep-hello-world-intellij'

bucket = s3.Bucket(bucket_name)

bucket.objects.all().delete()

bucket.delete()