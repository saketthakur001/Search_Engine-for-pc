f = open("C:\index\index_data.txt", "r")

text = []
video = ['mp4', 'mkv','ts', 'mov', 'flv', 'webm', 'gif', 'm4p', 'mpg', 'm4v']

folder_no = 0

# for i in f:
#     text.append(i)
#     (i)

for i in f:
    if "$" in i:
        continue
    elif "BIN" in i:
        continue
    else:
        text.append(i)
        # print(i)

for i in text:
    search1 = "a girl who loops through time.mp4"
    search = 'video'
    if search == 'video':
        for ii in video:
            
            if i in ii:
                print(i)
    
    elif search in i:
        if '\\' in i:
            continue
        else:
            print(i)
        # else:


#     if iteration == 10000:
#         break
#     iteration += 1

iteration = 1
# for i in text:
#     search = '.mp3'
#     '''work on it later'''
#     search = 'saket' #input('search: ')
#     for i in text:
#         print('working...')
#         print(iteration <= 500)
#         if search == "video":
#             print(iteration, ' is the iteration value')
#             iteration += 1
#             txt = i
#             i = i.split('.')
    #         i = i[-1]