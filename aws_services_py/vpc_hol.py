'''
Using Boto3 to create a VPC with a public subnet and a private subnet
'''

# Import statements
import boto3
import time

# Create VPC
ec2 = boto3.client('ec2')
vpc_name = "vpc-hol"

response = ec2.describe_vpcs(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [vpc_name]
        }
    ]
)
vpcs = response.get('Vpcs', [])
# print(vpcs)
if vpcs:
    vpc_id = vpcs[0]['VpcId']
    print(f"VPC '{vpc_name}' with id '{vpc_id}' already exists.")
else:
    vpc_response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = vpc_response['Vpc']['VpcId']
    time.sleep(5)
    ec2.create_tags(Resources=[vpc_id], Tags=[{'Key': 'Name', 'Value': vpc_name}])
    print(f"VPC '{vpc_name}' with id '{vpc_id}' has been created.")

# Create internet gateway
ig_name = 'ig-vpc-hol'
response = ec2.describe_internet_gateways(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [ig_name]
        }
    ]
)
igws = response.get('InternetGateways', [])
if igws:
    ig_id = igws[0]['InternetGatewayId']
    print(f"Internet Gateway '{ig_name}' with id '{ig_id}' already exists.")
else:
    ig_response = ec2.create_internet_gateway()
    ig_id = ig_response['InternetGateway']['InternetGatewayId']
    ec2.create_tags(Resources=[ig_id], Tags=[{'Key': 'Name', 'Value': ig_name}])
    ec2.attach_internet_gateway(InternetGatewayId=ig_id, VpcId=vpc_id)
    print(f"Internet Gateway '{ig_name}' with id '{ig_id}' has been created.")

# Create a route table and a public route
rt_response = ec2.create_route_table(VpcId=vpc_id)
rt_id = rt_response['RouteTable']['RouteTableId']
route = ec2.create_route(
    RouteTableId=rt_id,
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=ig_id
)
print(f"Route Table with id '{rt_id}' has been created with a route to the internet gateway '{ig_id}'.")

# Create 3 subnets
subnet_1 = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.1.0/24', AvailabilityZone='us-east-1a')
subnet_2 = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.2.0/24', AvailabilityZone='us-east-1b')
subnet_3 = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.3.0/24', AvailabilityZone='us-east-1c')

print(f"Subnet 1 with id '{subnet_1['Subnet']['SubnetId']}' has been created in availability zone '{subnet_1['Subnet']['AvailabilityZone']}'")
print(f"Subnet 1 with id '{subnet_2['Subnet']['SubnetId']}' has been created in availability zone '{subnet_2['Subnet']['AvailabilityZone']}'")
print(f"Subnet 1 with id '{subnet_3['Subnet']['SubnetId']}' has been created in availability zone '{subnet_3['Subnet']['AvailabilityZone']}'")
