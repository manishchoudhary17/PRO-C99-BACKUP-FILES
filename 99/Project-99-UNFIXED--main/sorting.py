#sorting everything into it's own folder
import os
import shutil

path = input("What's the folder that you would like to sort?")
present = os.path.exists(path)
if(present == False):
    print("That doesn't exist.")
else:
    listfiles = os.listdir(path)
    for file in listfiles:
        mainpart, extension= os.path.splitext(file)
        #: = everything from first thing in the list to the last thing in the list
        # :5 = everything from 1 to 5
        extension = extension[1:]
        print(extension)
        if(extension == ""):
            continue 
        if(os.path.exists(path+'/'+ extension)):
            shutil.move(path+"/"+ file, path+"/"+ extension + "/" + file)
        else:
            os.makedirs(path + "/" + extension)
            shutil.move(path+"/"+ file, path + "/" + extension +"/"+file)