from os import walk 
from os import path
# file types
video = ['mp4', 'mkv','ts', 'mov', 'flv', 'webm', 'gif', 'm4p', 'mpg', 'm4v']
pictures = ['apng', 'avif', 'gif', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'png', 'svg', 'webp']
audio = ['wav', 'ogg', 'mp3', 'gsm', 'dct', 'flac', 'aac', 'pcm', 'dsd', 'wma','alff' ]

commands = ['v', 'p', 'a', 't',]

#user name
username = path.expanduser("~").split('\\')[-1]
print('Hey',username, 'type .help for help')

# locations to search
drive_locations = [
    'D:\\',
    'C:\\Users\\' + username + '\\Desktop',
    'C:\\Users\\' + username + '\\Music',
    'C:\\Users\\' + username + '\\Pictures',
    'C:\\Users\\' + username + '\\Downloads',
    'C:\\Users\\' + username + '\\Documents'
]

def walking():
    
    lis = []
    for i in drive_locations:
        for root, dirs, files in walk(i):
            for i in files:
                if input_ in i.lower():
                    drive_loc = root[0:2]
                    lis.append(drive_loc+'\\'+root.strip(drive_loc)+'\\'+i)
    return lis

def simple_search():
    global file_lis
    for i in walking():
        if input_ in i:
            file_lis.append(i)

def video_search(input_):                
    global file_lis                      
    for i in walking():                  
        if i.split('.')[-1] in video:
            if input_ in i:   
                file_lis.append(i)       
                                         
def picture_search(input_):              
    global file_lis                      
    for i in walking():                  
        if i.split('.')[-1] in pictures:
            if input_ in i:             
                file_lis.append(i)   

def audio_search(input_):
    global file_lis
    for i in walking():
        if i.split('.')[-1] in audio:
            if input_ in i:
                file_lis.append(i)

def type_search(input_):
    global file_lis
    for i in walking():
        if i.split('.')[-1] == input_:
            if input_ in i:
                file_lis.append(i)

def folder_search():
    global file_lis
    for i in drive_locations:
        for root, dirs, file in walk(i):
            for i in dirs:
                if input_ in i:
                    file_lis.append(root+'\\'  +i)

def help_():
    global result
    result = False
    print(' v. for Video search\n',
           'p. for Picture search\n',
           'a. for Audio search\n',
           'f. for Folder saerch\n',
           't. for Type of file you want to search, exmaple- t.mp3'
        )

while True:
    result = True
    file_lis = []
    input_ = input('search: ')

# SEARCH - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # help -----------------------------------
    if '.help' in input_:
        print('.help activated')
        help_()

    # video search ---------------------------
    elif input_[0:2] == 'v.':
        print('video search activated')
        input_ = input_[2:]
        video_search(input_)

    # picture search -------------------------
    elif input_[0:2] == 'p.':
        print('picture search activated')
        input_ = input_[2:]
        picture_search(input_)

    # audio saerch ---------------------------
    elif input_[0:2] == 'a.':
        print('audio search activated')
        input_ = input_[2:]
        audio_search(input_)

    # type search ----------------------------
    elif input_[0:2] == 't.':
        print('type search activated')
        input_ = input_[2:]
        type_search(input_)

    # folder search --------------------------
    elif input_[0:2] == 'f.':
        print('file search activated')
        input_ = input_[2:]
        folder_search()

    # simple search --------------------------
    else:
        print('simple search')
        simple_search()
    if len(file_lis) > 9999:
        pass
    else:
        for i in file_lis:
            if not '\\\\' in i:
                print(i)
            else:
                print(i[:2]+i[3:])
    
    if len(file_lis) > 1:
        fi = 'files'
    else:
        fi = 'file'
    if result:
        print(len(file_lis), fi ,'found!')
