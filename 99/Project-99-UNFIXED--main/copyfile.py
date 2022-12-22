import os
import shutil

source = "test.txt"
destination = "copytest.txt"

result=shutil.copy(source,destination)
destination2 = "C:/Users/shahs/Downloads/newfolder"
print(result)
#moving the source to destination2
result2 = shutil.move(source,destination2)
print("Successfully moved!")
 