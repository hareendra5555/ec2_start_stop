import boto3

def lambda_handler(event, context):
    # Specify your region and instance IDs
    region = 'us-east-1'  # Replace with your AWS region
    instance_ids = ['i-0123456789abcdef0']  # Replace with your EC2 instance IDs

    ec2 = boto3.client('ec2', region_name=region)

    try:
        # Stop the instances
        response = ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Stopped instances: {instance_ids}")
        return response
    except Exception as e:
        print(f"Error stopping instances: {e}")
        raise e
