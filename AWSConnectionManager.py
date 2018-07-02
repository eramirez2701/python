import boto3


# Returns Boto3 session based on profile name
def get_boto3session(profile_name):
    return boto3.session.Session(profile_name=profile_name)


# Returns a client for an AWS service based on the provided service_name and region
def get_client(session, service_name, region):
    return session.client(service_name, region_name=region)
