from os import walk, path, system, listdir

# list of drives
import win32api
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]

for i in drives:
    try:
        for ii in listdir(i):
            if ii == 'Windows':
                drives.remove(i)
                drives.insert(0, i)
    except PermissionError:
        pass
username = path.expanduser("~").split('\\')[-1]
user_loc = drives[0]+'Users\\' + username
print(user_loc)
print(drives[0])
