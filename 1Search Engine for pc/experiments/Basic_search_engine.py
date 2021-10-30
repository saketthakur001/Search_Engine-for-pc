f = open("C:\index\index_data.txt", "r")
text = []
video = ['mp4', 'mkv','ts', 'mov', 'flv', 'webm', 'gif', 'm4p', 'mpg', 'm4v']

folder_no = 0

for i in f:
    if "$" in i:
        continue
    elif "BIN" in i:
        continue
    else:
        text.append(i)
loc = None
file = None
while True:
    s = input('search: ')

    for i in text:
        if s in i:
            file = i
            if '\\' in i:
                continue
            print(loc + file)
            # break
        if '\\' in i:
            loc = i
            loc = loc.replace('\n', '\\')
            lo = loc[0:2]+'\\'
            loc = lo+loc[2:]
    # print(loc+file)
