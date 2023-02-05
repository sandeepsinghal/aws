import boto3

ec2 = boto3.resource('ec2', region_name='us-west-2a')

print(ec2)
