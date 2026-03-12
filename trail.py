import s3enforce
import json
import boto3

# Creates Cloudtrail for logging
def CreateTrail(trail_name, bucket_name):
    cloudtrail_client = boto3.client('cloudtrail')
    try:
        response = cloudtrail_client.create_trail(
            Name=trail_name,
            S3BucketName=bucket_name,
        )
        cloudtrail_client.start_logging(Name=trail_name)
        return response
    except cloudtrail_client.exceptions.TrailAlreadyExistsException:
        cloudtrail_client.start_logging(Name=trail_name)

# Starts logging
def StartLogging(trail_name):
    cloudtrail_client = boto3.client('cloudtrail')
    cloudtrail_client.start_logging(Name=trail_name)

# Stops logging
def StopLogging(trail_name):
    cloudtrail_client = boto3.client('cloudtrail')
    cloudtrail_client.stop_logging(Name=trail_name)

# Gets status with exception handling
def GetTrailStatus(trail_name):
    cloudtrail_client = boto3.client('cloudtrail')
    try:
        response = cloudtrail_client.get_trail_status(Name=trail_name)
        return response['IsLogging']
    except cloudtrail_client.exceptions.TrailNotFoundException:
        raise NameError("That Cloutrail Trail was not found")

# Main function setup for Cloudtrial start/stop logging
def main():
    sts_client = boto3.client("sts")
    account_id = sts_client.get_caller_identity()["Account"]
    bucket_name = "rvanovermeiren-cloud-trail-versioning-demo"
    trail_name = "rvanovermeiren-ct-demo"

    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AWSCloudTrailAclCheck20150319",
                "Effect": "Allow",
                "Principal": {"Service": "cloudtrail.amazonaws.com"},
                "Action": "s3:GetBucketAcl",
                "Resource": f"arn:aws:s3:::{bucket_name}"
            },
            {
                "Sid": "AWSCloudTrailWrite20150319",
                "Effect": "Allow",
                "Principal": {"Service": "cloudtrail.amazonaws.com"},
                "Action": "s3:PutObject",
                "Resource": f"arn:aws:s3:::{bucket_name}/AWSLogs/{account_id}/*",
                "Condition": {"StringEquals": {"s3:x-amz-acl": "bucket-owner-full-control"}}
            }
        ]
    }
    
    s3enforce.CreateBucket(bucket_name)
    s3enforce.SetBucketPolicy(bucket_name, json.dumps(policy))
    CreateTrail(trail_name, bucket_name)
    
    StopLogging(trail_name)
    
    # Checks status and starts logging
    if not GetTrailStatus(trail_name):
        StartLogging(trail_name)
    else:
        print("Logging is already enabled.")

if __name__ == "__main__":
    main()