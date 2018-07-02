import AWS.Connection.AWSConnectionManager as ConnectionManager
import AWS.EC2.InstanceManager as InstanceManager


session = ConnectionManager.get_boto3session('default')
ec2 = ConnectionManager.get_client(session, 'ec2', 'us-east-1')
filter = [{'Name': 'instance-state-name',
           'Values': ['running']}]
running_instances = InstanceManager.filter_instances(ec2, filter)
print(running_instances)
