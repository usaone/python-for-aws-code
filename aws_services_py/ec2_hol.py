'''
This script manages Amazon EC2 instances using the Boto3 Python SDK
'''
# Import statements
import boto3

# Create ec2 resource and instance name
ec2_resource = boto3.resource('ec2')
instance_name = 'my_instance'

# Store instance id
instance_id = None

# Check if instance that you are trying to create already exists
# and only work with an instance that hasn't be terminated
instances = ec2_resource.instances.all()
instance_exists = False
for instance in instances:
    if instance.tags is not None and instance.state['Name'] not in ['terminated']:
        for tag in instance.tags:
            if tag['Key'] == 'Name' and tag['Value'] == instance_name:
                instance_id = instance.id
                instance_exists = True
                print(f"An instance named '{instance_name}' with id '{instance_id}' already exists.")
                break
    if instance_exists:
        break


# Launch a new EC2 instance if it hasn't already been created
if not instance_exists:
    new_instance = ec2_resource.create_instances(
        ImageId='ami-06c68f701d8090592', # Amazon Linux 2023 AMI 2023.5.20240701.0 x86_64 HVM kernel-6.1
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='uddip_key',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name
                    }
                ]
            }
        ]
    )
    instance_id = new_instance[0].id
    print(f"Instance named '{instance_name}' with id '{instance_id}' created.")

# Stop an EC2 instance
print("States for the instance are: ",ec2_resource.Instance(instance_id).state)
if ec2_resource.Instance(instance_id).state['Name'] == 'running':
    ec2_resource.Instance(instance_id).stop()
    print(f"Instance '{instance_name}-{instance_id}' has been stopped.")

# Start an EC2 instance
if ec2_resource.Instance(instance_id).state['Name'] == 'stopped':
    ec2_resource.Instance(instance_id).start()
    print(f"Instance '{instance_name}-{instance_id}' has been started.")

# Terminate an EC2 instance
ec2_resource.Instance(instance_id).terminate()
print(f"Instance '{instance_name}-{instance_id}' has been terminated.")
