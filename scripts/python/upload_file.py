# Upload file to S3 under a certain bucket and return a public url 
import sys

import boto3
from botocore.exceptions import NoCredentialsError

s3 = boto3.client('s3')
bucket_name = 'chatgpt'

""" if len(sys.argv) < 2:
    print("Please provide the file name as a command line argument.")
    sys.exit(1)
 """
#file_name = sys.argv[1]
file_name = 'temp.py'

try:
    s3.upload_file(file_name, bucket_name, file_name)
    print("Upload Successful")
except FileNotFoundError:
    print("The file was not found")
except NoCredentialsError:
    print("Credentials not available")

bucket_location = s3.get_bucket_location(Bucket=bucket_name)
object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(bucket_location['LocationConstraint'], bucket_name, file_name)

print(object_url)