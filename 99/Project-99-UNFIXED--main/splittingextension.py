import os
path="C:/Users/shahs/Downloads/newfolder"
#splitting the extension from the main file
result=os.path.splitext(path)
print(result)
print("Main path: ", result[0])
print("extension: ", result[1])    
print("What's inside: ",os.listdir(path))

