# Import the boto3 library
import boto3

# Instantiate a boto3 resource for S3 and name your bucket
s3 = boto3.resource('s3')
bucket_name = 'unique-bucket-name-1234567890'

# Check if bucket exists
# Create the bucket if it does NOT exist
all_my_buckets = [bucket_name for bucket in s3.buckets.all()]
if bucket_name not in all_my_buckets:
    print(f'{bucket_name} bucket does not exist. Creating now...')
    s3.create_bucket(Bucket=bucket_name)
    print(f'{bucket_name} bucket has been created.')
else:
    print(f'{bucket_name} bucket already exists. No need to create new one.')
# Create 'file_1' and 'file_2'
# UPLOAD 'file_1' to the new bucket


# READ and print the file from the bucket


# UPDATE 'file_1' in the bucket with new content from 'file_2'


# DELETE the file from the bucket


# DELETE the bucket (the bucket should be empty.)
