import boto3

#Create a new S3 bucket with the given name
def CreateBucket(bucket_name):
   s3client = boto3.client('s3')
   response = s3client.create_bucket(Bucket=bucket_name)
   return response

#Delete the S3 bucket with the given name
def DeleteBucket(bucket_name):
   s3client = boto3.client('s3')
   response = s3client.delete_bucket(Bucket=bucket_name)
   return response

#Enable versioning for the specified S3 bucket
def EnforceVersioning(bucket_name):
   s3client = boto3.client('s3')
   response = s3client.put_bucket_versioning(
       Bucket=bucket_name,
       VersioningConfiguration={
           'MFADelete': 'Disabled',
           'Status': 'Enabled',
       },
   )
   return response

#Set the policy for the specified S3 bucket
def SetBucketPolicy(bucket_name, policy):
   s3client = boto3.client('s3')
   response = s3client.put_bucket_policy(Bucket=bucket_name, Policy=policy)
   return response

# Main function to create the bucket and enforce versioning
def main():
   bucket_name = "rvanovermeiren-cloud-trail-versioning-demo"
   response = CreateBucket(bucket_name)
   version_response = EnforceVersioning(bucket_name)

if __name__ == "__main__":
    main()