import boto3
region = 'us-east-1'
instances = ['i-0a15bc3758b0e649d', 'i-0bbdf014d7762b643']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))
