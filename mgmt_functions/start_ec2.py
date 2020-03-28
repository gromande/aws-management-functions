import boto3
from functions import get_ec2_instance_ids

region = 'us-east-1'
instances = get_ec2_instance_ids('us-east-1')
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))
