import boto3
import os

client = boto3.client('ec2')

regions = []
if 'EC2_REGION' in os.environ:
    regions = [os.environ['EC2_REGION']]
else:
    regions = [region['RegionName'] for region in client.describe_regions()['Regions']]

tag = os.environ['EC2_TAG'] if 'EC2_TAG' in os.environ else None

def start_lambda_handler(event, context):
    managed_ec2_instances('start')

def stop_lambda_handler(event, context):
    managed_ec2_instances('stop')

def managed_ec2_instances(action):
    for region in regions:
        print("Region: ", region)
        ec2 = boto3.resource('ec2', region_name=region)
        instances = ec2.instances.filter(Filters=[{'Name' :'tag:' + tag, 'Values':[''] }]) if tag else ec2.instances.all()
        for instance in instances:
            print("Instance ID: %s. Action: %s" % (instance.id, action))
            if action == 'start':
                instance.start()
            elif action == 'stop':
                instance.stop()
            else:
                raise Exception('Unknown action')
