import boto3
import csv
from datetime import datetime

def lambda_handler(event, context):
    
    # Initialize the s3 resource using boto3
    s3 = boto3.resource('s3')

    # Extract the bucket name and the CSV file from the 'event input
    billing_bucket = event['Records'][0]['s3']['bucket']['name']
    csv_file = event['Records'][0]['s3']['object']['key']

    # Define the name of the error bucket where you want to copy the erroneous CSV files
    error_bucket = 'uddip-s3-billing-errors-2024-07-12'

    # Download the CSV file from S3, read the content, decode from bytes to string, and split the content by lines
    obj = s3.Object(billing_bucket, csv_file)
    data = obj.get()['Body'].read().decode('utf-8').splitlines()

    # Intialize a flag (error_found) to false. We'll set this flag to true when we find an error
    error_found = False

    # Define valid product lines and valid currencies
    valid_product_lines = ['Bakery', 'Meat', 'Dairy']
    valid_currencies = ['USD', 'MXN', 'CAD']

    # Read the CSV content line by line using Python's CSV reader. Ignore the header line (data[1:])
    for row in csv.reader(data[1:], delimiter=','):
        print(f"row: {row}")
        # For each row, extract the product line, currency, bill amount, and date from the specific columns

        # Check if the product line is valid. If not, set the error flag to true and print an error message

        # Check if the currency is valid. If not, set the error flag to true and print an error message

        # Check if the bill amount is negative. If so, set the error flag to true and print an error message

        # Check if the date is in the correct format ('%Y-%m-%d'). If not, set the error flag to true and print an error message

    # After checking all rows, if an error is found, copy the CSV file to the error bucket and delete it from the original bucket

        # Handle any exception that may occur while moving the file, and print the error message
        
    # If no errors were found, return a success message with status code 200 and a body message indicating that no errors were found

    return {
        'statusCode': 200,
        'body': json.dumps('No errors found in the CSV file.')
    }'
    }

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
