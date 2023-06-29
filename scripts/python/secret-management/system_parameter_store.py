#https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-app-ssm-paramstore.html

import boto3

def store_credentials_in_parameter_store(key, value):
    # Create a Boto3 client for AWS Systems Manager
    ssm_client = boto3.client('ssm')
    
    # Specify the parameter name for the key
    key_param_name = '/myapp/credentials/key'
    
    # Specify the parameter name for the value
    value_param_name = '/myapp/credentials/value'
    
    # Store the key parameter
    ssm_client.put_parameter(
        Name=key_param_name,
        Value=key,
        Type='SecureString',
        Overwrite=True
    )
    
    # Store the value parameter
    ssm_client.put_parameter(
        Name=value_param_name,
        Value=value,
        Type='SecureString',
        Overwrite=False
    )

# Usage example
key = 'my_key'
value = 'my_value'
store_credentials_in_parameter_store(key, value)

print ("completed")