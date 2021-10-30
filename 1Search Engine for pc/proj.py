from datetime import datetime
from os import walk

today = str(datetime.now())

recent = r"C:\Users\saket\Recent"
f_loc = "C:\index\index_data.txt"
f = open(f_loc, "r+")

def drive_iteration(loc):
    # f.write(today + '\n')
    # dir = walk(loc)
    count = 0
    file_lis = []

    for root, dirs, files in walk(loc):
        for i in files:
            if input_ in i.lower():
                drive_loc = root[0:2]
                file_lis.append(drive_loc+'\\'+root.strip(drive_loc)+'\\'+i)
    if len(file_lis) == 0:
        print('NO RESULT FOUND!')
    if len(file_lis) > 99999:
        # for i in file_lis:
            # if input_[0]
            pass

    else:
        for i in file_lis:
            print(i)
    if len(file_lis) > 1: fi = 'files'
    else: fi = 'file'
    print(len(file_lis), fi ,'found!')
while True:
    input_ = input('search: ')
    drive_iteration('D:')

def additional_feature_scan():
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