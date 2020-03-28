import boto3

def get_ec2_instance_ids(region, state):
    ec2 = boto3.resource('ec2', region_name=region)
    #ec2_instance_ids = []
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': [state]}])
    ec2_instance_ids = [instance.id for instance in instances]
    return ec2_instance_ids

def get_ec2_instance_ids(region):
    ec2 = boto3.resource('ec2', region_name=region)
    #ec2_instance_ids = []
    instances = ec2.instances.all()
    ec2_instance_ids = [instance.id for instance in instances]
    return ec2_instance_ids
