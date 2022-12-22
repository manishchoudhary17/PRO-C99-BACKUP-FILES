import os
# os.mkdir("C:/Users/shahs/Downloads/newfolder")
test=os.getcwd()
print(test)
path="C:/Users/shahs/Downloads/notafolder"

present= os.path.exists(path)

print(present)

if(present == True):
    print("Exists")
else:
    print("Does not exist")