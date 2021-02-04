#!/usr/bin/env python3

import boto3

ec2=boto3.resource('ec2',region_name="us-east-1")


data = ec2.vpcs.filter(Filters=[{'Name':'isDefault','Values':["true"]}]).limit(count=1)

for vpc in data:
        vpc_id=vpc.vpc_id

instances=ec2.instances.filter(Filters=[{'Name':'vpc-id', 'Values':[vpc_id]},{'Name':'instance-type','Values':['m5.large']}])
print(f'{"NAME":<20} {"ID":<20} {"PUBLIC_IP":<15} {"STATE":<15}')
print("="*70)

for instance in instances:
        name = [i['Value'] for i in instance.tags if i['Key'] == 'Name']
        if not name:
          name = "-"
        else:
          name=name[0]
        print(f"{name:<20} {instance.id:<20} {instance.public_ip_address:<15} {instance.state['Name']:<15}")
