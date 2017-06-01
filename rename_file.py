import os

def rename_files():
    display_files = os.listdir(r"C:\Users\AdithyaMaheshBariki\Downloads\prank\prank")
    print(display_files)
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\AdithyaMaheshBariki\Downloads\prank\prank")
    for file_name in display_files:
        print("old name" +file_name)
        print("new name" +file_name.translate(None, "1234567890")
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_files()
