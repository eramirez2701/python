import boto3
from botocore.exceptions import ClientError


def create_instance(ec2_session, ami_id, min_count, max_count, instance_type, key_name):
    return ec2_session.create_instance(
        ImageId=ami_id,
        MinCount=min_count,
        MaxCount=max_count,
        KeyName=key_name,
        InstanceType=instance_type
    )


def filter_instances(ec2_client, custom_filter):
    try:
        filtered_instances = ec2_client.describe_instances(Filters=custom_filter)
        instances = {}
        if not filtered_instances["Reservations"]:
            return print("List is empty")
        else:
            for reservation in filtered_instances["Reservations"]:
                for instance in reservation["Instances"]:
                    instances[instance["InstanceId"]] = instance
        return instances
    except ClientError as e:
        print("Error while filtering: ", e)