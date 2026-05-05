# calling functions created in aws.py

# from aws import *  # this imports all functions 
from aws import create_bucket,list_bucket,del_bucket # this import required funt via list


# for creating bucket
# option 1
nameb = input("Enter the bucketname to create: ").lower().strip()
create_bucket(nameb)
# option 2
# pass the value in the function to create the bucket
# create_bucket("testing-create-bucket-via-fucntion")

value = list_bucket()
# print(value)


# delete bucket function test
# option 1
name = input("Enter the bucket to deletion: ").lower().strip()
del_bucket(name)

# option 2
# It will delete all buckets 
# Delete function will only work if there will be any bucket available
#for name in value["Buckets"]:
#    crap = name["Name"]
#    print(f"The bucket to be delete: {crap}")
#    del_bucket(crap)
#    print(f"Bucket Deleted: {crap} via Test.py")
