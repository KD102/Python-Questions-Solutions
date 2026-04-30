import os

# set to file path which one you shoude show 
path = "/Users/Kenil/Videos/Captures"

# get List data From os 
content = os.listdir(path)

# print content to hear 
for i in content:
    print(i)

