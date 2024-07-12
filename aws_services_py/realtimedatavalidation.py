# Import the boto3 library
import boto3

# Instantiate a boto3 resource for S3 and name your bucket
s3 = boto3.resource('s3')
bucket_name1 = 'uddip-s3-billing-2024-07-12'
bucket_name2 = 'uddip-s3-billing-errors-2024-07-12'

def check_bucket_exists(bucket):
    all_my_buckets = [bucket for bucket in s3.buckets.all()]
    if bucket not in all_my_buckets:
        return False
    else:
        return True

if not check_bucket_exists(bucket_name1):
    print(f'{bucket_name1} bucket does not exist. Creating now...')
    s3.create_bucket(Bucket=bucket_name1)
    print(f'{bucket_name1} bucket has been created.')
else:
    print(f'{bucket_name1} bucket already exists. No need to create a new one.')

if not check_bucket_exists(bucket_name2):
    print(f'{bucket_name2} bucket does not exist. Creating now...')
    s3.create_bucket(Bucket=bucket_name2)
    print(f'{bucket_name2} bucket has been created.')
else:
    print(f'{bucket_name2} bucket already exists. No need to create a new one.')

# DELETE the bucket (the buckt should be empty.
# bucket1 = s3.Bucket(bucket_name1)
# bucket1.delete()
# bucket2 = s3.Bucket(bucket_name2)
# bucket2.delete()
