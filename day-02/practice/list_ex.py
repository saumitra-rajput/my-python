a = (1,2,3, True, 2.3) # first method
print(a)

cloud = list() # second method

print(type(cloud))

cloud.append("aws")
cloud.append("azure")
cloud.append("gcp")

print(cloud)
print("Length of list is : ", len(cloud))
print("World leaders for cloud: ", cloud[0])

print(dir(cloud))



for csp in cloud:
    if csp == "aws":
        print(f"{csp} Market Leader")
    elif csp == "azure":
        print(f"{csp} Another major Enterprise cloud")
    else:
        print(f"{csp} Other best")

