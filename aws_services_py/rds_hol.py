'''
RDS Hands-On Lab Using Boto3
'''
import boto3
import time
import botocore
import botocore.exceptions

# Instantiate a boto3 client for RDS
rds = boto3.client('rds')

# DB Credentials
username='uddipadmin'
password='U1x2h$n9'


# Create DB Subnet Group
db_subnet_group = 'rds-uddip-subnet-group'
try:
    response = rds.create_db_subnet_group(
        DBSubnetGroupName='rds-uddip-subnet-group',
        DBSubnetGroupDescription='Subnet group for RDS Hands-On Lab',
        SubnetIds=[
            'subnet-035a7a580710a6bf5',
            'subnet-02c1907885479f6f8',
            'subnet-076e213bede100ac0'
        ]
    )
    db_subnet_group = response['DBSubnetGroup']['DBSubnetGroupName']
    print(f'DB Subnet Group created: {db_subnet_group}')
except rds.exceptions.DBSubnetGroupAlreadyExistsFault as e:
    print(f"DB subnet group '{db_subnet_group}' already exists")
    # Temporarily ignore the error if the subnet group already exists


# Create the DB Cluster
db_cluster_id = 'rds-uddip-cluster'
try:
    response = rds.create_db_cluster(
        DBClusterIdentifier=db_cluster_id,
        Engine='aurora-mysql',
        EngineVersion='5.7.mysql_aurora.2.12.3',
        EngineMode='serverless',
        DatabaseName='uddipdb',
        MasterUsername=username,
        MasterUserPassword=password,
        DBSubnetGroupName=db_subnet_group,
        EnableHttpEndpoint=True,
        ScalingConfiguration={
            'AutoPause': True,
            'MaxCapacity': 8,
            'MinCapacity': 1,
            'SecondsUntilAutoPause': 300
        }
    )
    print(f'DB Cluster created: {db_cluster_id}')
except rds.exceptions.DBClusterAlreadyExistsFault as e:
    print(f"DB cluster '{db_cluster_id}' already exists")
except rds.exceptions.DBSubnetGroupAlreadyInUse as e:
    print(f"DB subnet group '{db_subnet_group}' is already in use")

# Wait for the DB cluster to become available
waiter = rds.get_waiter('db_cluster_available')
waiter.wait(DBClusterIdentifier=db_cluster_id)
print(f'DB Cluster is now available: {db_cluster_id}')

# Modify the DB cluster. Update the scaling configuration for the cluster
response = rds.modify_db_cluster(
    DBClusterIdentifier=db_cluster_id,
    ScalingConfiguration={
        'AutoPause': True,
        'MaxCapacity': 16,
        'MinCapacity': 1,
        'SecondsUntilAutoPause': 600
    }
)
print(f'DB Cluster scaling configuration updated: {db_cluster_id}')


# Delete the DB cluster
response = rds.delete_db_cluster(
    DBClusterIdentifier=db_cluster_id,
    SkipFinalSnapshot=True)
print(f'DB Cluster is being deleted: {db_cluster_id}')

# Wait for the DB cluster to be deleted
start_time = time.time()
waiter = rds.get_waiter('db_cluster_deleted')
waiter.wait(DBClusterIdentifier=db_cluster_id)
print(f'DB Cluster is now deleted: {db_cluster_id}')

# Todo:
# Create tables in the database
# Add data to the tables
# Query the tables
# Drop the tables
