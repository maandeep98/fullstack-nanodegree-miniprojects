import os

def rename_files():
    # get file names
    file_list = os.listdir(r"C:\Users\Hp\Desktop\python\prank")
    print(file_list)
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir(r"C:\Users\Hp\Desktop\python\prank")
    # rename files
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None , "0123456789"))
        print(file_name)
    os.chdir(saved_path)
    
rename_files()
