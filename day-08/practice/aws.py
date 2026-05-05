# This script has Amazon S3 bucket operation functions can be called in other python scripts
# Requirement: AWS CLI configured with the amazon s3 access for now


import boto3
connection = boto3.client("s3")

# Example to get Bucket names

def list_bucket():
    data = connection.list_buckets()
    
    if data["Buckets"]:
        for bucket in data["Buckets"]:
            print(f"The Bucket name is : {bucket['Name']}")
    else:
        print("Nothing to show: No bucket found.")
    return data


# Example to Create bucket

def create_bucket(name):
    bucket_name = name.lower().strip()

    if len(bucket_name) > 0:
        try:
            connection.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    "LocationConstraint": "us-east-2"
                 })
            print(f"Bucket created successfully:{bucket_name}")
    
        except Exception:
            print(f"Bucket already exists {bucket_name} or Error occured..")
    else:
        print("Invalid input..")


# Example for delete amazon bucket

def del_bucket(name):
    bucket_del = name.lower().strip()

    if bucket_del:
        try:
            # getting the all files and data of bucket

            buck_data = connection.list_objects_v2(Bucket=bucket_del)

            # check and del any files
        
            if "Contents" in buck_data:
                for files in buck_data["Contents"]:
                    connection.delete_object(Bucket=bucket_del, Key=files["Key"])
        
            # delete the bucket

            connection.delete_bucket(Bucket=bucket_del)
            print(f"Bucket Deleted: {bucket_del}")

        except Exception:
            print("Error occured")
    else:
        print("Invalid Input.")

