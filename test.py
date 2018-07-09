import AWS.Connection.AWSConnectionManager as ConnectionManager
import AWS.EC2.InstanceManager as InstanceManager


ec2 = ConnectionManager.get_client('default', 'ec2', 'us-east-1')
running_filter = [{'Name': 'instance-state-name',
                   'Values': ['running']}]
running_instances = InstanceManager.filter_instances(ec2, running_filter)
print(running_instances)