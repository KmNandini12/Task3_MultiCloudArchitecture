import boto3

s3 = boto3.client(
    's3',
    aws_access_key_id='YOUR_ACCESS_KEY', #Used the access key from AWS IAM nandiniemp
    aws_secret_access_key='YOUR_SECRET_KEY', #Used the secret key from AWS IAM nandiniemp
    region_name='ap-south-1'
)

response = s3.list_objects_v2(Bucket='codetech-internship-bucket')
for obj in response.get('Contents', []):
    print(obj['Key'])
