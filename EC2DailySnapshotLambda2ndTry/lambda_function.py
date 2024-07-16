import json
import boto3
import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Log the entire event to verify its structure
    logger.info(f'Received event: {json.dumps(event)}')

    try:
        # Access volume_id from the event
        volume_id = event["volume_id"]
        logger.info(f'Creating snapshot for volume: {volume_id}')

        response = ec2.create_snapshot(
            VolumeId=volume_id,
            Description='My EC2 Snapshot',
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': f'My EC2 Snapshot-{volume_id}-{current_date}'
                        },
                    ]
                },
            ],
        )

        logger.info(f'Successfully created snapshot: {json.dumps(response, default=str)}')

    except KeyError as e:
        logger.error(f'Key error: {str(e)} - Check that the event contains the correct keys.')
    except Exception as e:
        logger.error(f'Error creating snapshot: {str(e)}')
