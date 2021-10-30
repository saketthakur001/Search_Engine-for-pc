import os
# programs = r'C:\Program Files'
programs = 'D:'

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
def filter(num, dig):
    if num % 10 == 0:
        print(dig)
        num += 1

f = os.walk(programs)
# try:
    # def drive_iteration(loc):
    #     dir = os.walk(loc)
    #     num = 1
    #     for i in dir:
    #         if can_iterate(i):
    #             for ii in i:
    #                 if can_iterate(ii):
    #                     for iii in ii:
    #                         if can_iterate(iii):
    #                             for iv in iii:
    #                                 if root_file(iv):
    #                                     break
    #                                 # f.write(iv+'\n')
    #                                 filter(num, iv)
                                    
    #                         else:
    #                             try:
    #                                 if root_file(iii):
    #                                     break
    #                                 # f.write(iii+'\n')
    #                                 filter(num, iii)
    #                             except UnicodeEncodeError:
    #                                 pass
    #                 else:
    #                     if root_file(ii):
    #                         break
    #                     # f.write(ii+'\n')
    #                     filter(num, ii)
    #         else:
    #             if root_file(i):
    #                 break
    #             # f.write(i+'\n')
    #             filter(num, i)
    # drive_iteration(f)

num = 1
for i in f:
    if num % 10 == 0:
        print(num, i)
    num += 1
