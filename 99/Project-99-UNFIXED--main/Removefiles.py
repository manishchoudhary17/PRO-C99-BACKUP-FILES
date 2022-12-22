import time
import os
import shutil

def main():
    path = "C:/Users/shahs/Downloads/New Folder (2)"
    deletedfolder = 0
    deletedfile = 0
    days = 30
    seconds= time.time() - days*24*60*60
    present = os.path.exists(path)
    if(present == False):
       print("Not a file!")
    else:
        for root_folder, folders,files in os.walk(path):
            if(seconds>=get_file_or_folder_age(root_folder)):
                remove_folder(root_folder)
                deletedfolder += 1
                print("DONE!")
                break
            else:
                for folder in folders:
                    folder_path= os.path.join(root_folder, folder)
                if(seconds>=get_file_or_folder_age(path)):
                    deletedfolder+=1
                    print("HELLO!")
            for file in files:
                file_path = os.path.join(root_folder, file)
                if(seconds>=get_file_or_folder_age(file_path)):
                    remove_file(file_path)
                    deletedfile +=1
                else:
                    if(seconds>=get_file_or_folder_age(path)):
                        remove_file(path)
                        deletedfile+=1

def remove_folder(path):

 	if not shutil.rmtree(path):

 		print(f"{path} is removed successfully")

	else:

 		print(f"Unable to delete the "+path)



def remove_file(path):

 	if not os.remove(path):

 		print(f"{path} is removed successfully")

	else:

 		print("Unable to delete the "+path)


def get_file_or_folder_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime

main()
 