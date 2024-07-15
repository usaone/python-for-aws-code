# Import the boto3 library
import boto3

# Instantiate a boto3 resource for S3 and name your bucket
s3 = boto3.resource('s3')
bucket_name1 = 'uddip-s3-billing-2024-07-12'
bucket_name2 = 'uddip-s3-billing-errors-2024-07-12'

def check_bucket_exists(buck):
    # all_my_buckets = list()
    all_my_buckets = [bucket.name for bucket in s3.buckets.all()]
    # for bucket in s3.buckets.all():
    #     print(bucket.name)
    #     all_my_buckets.append(bucket.name)

    if buck in all_my_buckets:
        return True
    else:
        return False

# print(check_bucket_exists(bucket_name1))
# print(check_bucket_exists(bucket_name2))

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

# # UPLOAD 'file_1' to the new bucket
# file_1 = 'billing_data_bakery_may_2023.csv'
# s3.Bucket(bucket_name1).upload_file(Filename=file_1, Key='billing_data_bakery_may_2023')
# print(f'{file_1} has been uploaded to {bucket_name1} bucket.')

# UPLOAD 'file_2' to the new bucket
file_2 = 'billing_data_dairy_may_2023.csv'
s3.Bucket(bucket_name1).upload_file(Filename=file_2, Key='billing_data_dairy_may_2023')
print(f'{file_2} has been uploaded to {bucket_name1} bucket.')

# # UPLOAD 'file_3' to the new bucket
# file_3 = 'billing_data_meat_may_2023.csv'
# s3.Bucket(bucket_name1).upload_file(Filename=file_3, Key='billing_data_meat_may_2023')
# print(f'{file_3} has been uploaded to {bucket_name1} bucket.')

# DELETE the bucket (the buckt should be empty.
# bucket1 = s3.Bucket(bucket_name1)
# bucket1.delete()
# bucket2 = s3.Bucket(bucket_name2)
# bucket2.delete()
