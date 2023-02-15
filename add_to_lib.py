import os
import shutil



#########################
## ADD YOUR FILES HERE ##
#########################
files_to_add_to_lib = ["ez_pdf.py"]
#########################



# Go to the folder where the python file is executed
# This way, if the python file is called from a command line,
# the relative filepaths will have the folder of the python file as a refence 
# and not the folder from which the command line is opened
file_path = os.path.dirname(__file__)
if file_path != "" :
    os.chdir(file_path)

# try to import notify lib
# if this fails, the errors will be redirected to a file instead
notify = True
try:
    from notifypy import Notify
    import notifypy
#except ModuleNotFoundError :
except :
    notify = False
    import sys
    sys.stderr = open('erreur_add_to_lib.txt', 'w')


# function that does the actual copy of the file to the lib folder
def add_file_to_lib(input_files) : 
    # find the lib folder
    lib_path = os.path.dirname(os.__file__)
    # do the copy
    for file in input_files :
        shutil.copy(file, lib_path)



if notify == True :
    notif = Notify()
    try:
        add_file_to_lib(files_to_add_to_lib)

        # if no errors, send a winows notif
        notif.title = 'add_to_lib.py | Successfull execution'
        notif.message = 'The Python files can now be imported as libraries'

        # try to add a fancy windows icon, if not possible, it's ok
        # a default one will be used by notifypy
        try :
            notif.icon = r"C:\Windows\System32\@WindowsHelloFaceToastIcon.png"
        except notifypy.exceptions.InvalidIconPath :
            None

        # send the notification
        notif.send(block=False)
    except BaseException as error :

        # if error, send a winows notif
        notif.title = 'add_to_lib.py | ERROR'
        notif.message = type(error).__name__

        # try to add a fancy windows icon, if not possible, it's ok
        # a default one will be used by notifypy
        try :
            notif.icon = r"C:\Windows\System32\SecurityAndMaintenance_error.png"
        except notifypy.exceptions.InvalidIconPath :
            None

        # send the notification
        notif.send(block=False)

        # Also raise the error for good measure
        raise(error)
else :
    # Here no notifications can be send because the lib could not be loaded
    try:
        add_file_to_lib(files_to_add_to_lib)
    except BaseException as error :
        print(type(error).__name__+": ",end="")
        print(error)
        raise(error)

