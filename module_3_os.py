import os
if os.path.exists("myfolder"):
    print("Already !!!")
else:
    os.mkdir("myfolder")

if os.path.exists("myfolder"):
    os.rmdir("myfolder")
else:
    print("not ")