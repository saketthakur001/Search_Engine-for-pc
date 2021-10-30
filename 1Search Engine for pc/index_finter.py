from datetime import datetime
from os import walk

today = str(datetime.now())

f_loc = "C:\index\index_data.txt"
f = open(f_loc, "r+")

def can_iterate(ex):
    if type(ex) == list:
        return True
    elif type(ex) == tuple:
        return True

def iterate(ex):
    for i in ex:
        return  

def root_file(file):
    if file[0] == "$":
        return True

def drive_iteration(loc):
    f.write(today + '\n')
    dir = walk(loc)
    for i in dir:
        if can_iterate(i):
            for ii in i:
                if can_iterate(ii):
                    for iii in ii:
                        if can_iterate(iii):
                            for iv in iii:
                                if root_file(iv):
                                    break
                                f.write(iv.lower() + '\n')
                                # print(iv)
                        else:
                            try:
                                if root_file(iii):
                                    break
                                f.write(iii.lower() + '\n')
                                # print(iii)
                            except UnicodeEncodeError:
                                pass
                else:
                    if root_file(ii):
                        break
                    f.write(ii.lower() + '\n')
                    # print(ii)
        else:
            if root_file(i):
                break
            f.write(i.lower() + '\n')

last_scan = f.readline()
if len(last_scan) < 1:
    print('working len')
    drive_iteration('D:')
f = open(f_loc, 'r+')
last_scan = f.readline()
last_scan = {'year' : int(last_scan[0:4]),
            'month' : int(last_scan[5:7]),
            'day'   : int(last_scan[8:10]),
            'hour'  : int(last_scan[11:13]),
            'minute': int(last_scan[14:16]),
            'second': int(last_scan[17:19])
            }

today = {'year' : int(today[0:4]),
        'month' : int(today[5:7]),
        'day'   : int(today[8:10]),
        'hour'  : int(today[11:13]),
        'minute': int(today[14:16]),
        'second': int(today[17:19])
        }
print(today, last_scan)
if today['day'] - last_scan['day'] > 1:
    drive_iteration("D:")

f.close()
f = open(f_loc, 'r+')

text = []
for i in f:
    if "$" in i:
        continue
    elif "BIN" in i:
        continue
    else:
        text.append(i)

while True:
    input_ = 'hey' #input()
    for i in text:
        if '\\' in i:
            loc = i
        if input_ in i:
            drive_loc = loc[0:2]
            loc = loc.strip('\n').strip(drive_loc)
            loc = drive_loc.upper()+"\\"+loc
            print(loc,i)
            break
    print('last scanned', today['hour'] - last_scan['hour'], 'hours ago')
    break
f.close()