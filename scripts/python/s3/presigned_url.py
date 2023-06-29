import boto3

s3 = boto3.client('s3')

bucket_name = 'chatgpt-sandeep'
object_key = 'offers.html'

url = s3.generate_presigned_url(
    ClientMethod='get_object',
    Params={
        'Bucket': bucket_name,
        'Key': object_key
    },
    ExpiresIn=3600  # URL expires in 1 hour
)

print(f"Public URL for S3 object '{object_key}':\n{url}")