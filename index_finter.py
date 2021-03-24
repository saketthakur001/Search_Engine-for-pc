import os


dir = []
f = open("C:\index\index_data.txt", "w+")

def can_iterate(ex):
    if type(ex) == list:
        return True
    elif type(ex) == tuple:
        return True

# def et(z):
#     if can_iterate:
#         for i in z:
#             return i
        
def iterate(ex):
    for i in ex:
        return  
def root_file(file):
    if file[0] == "$":
        return True
    
def drive_iteration(loc):
    dir = os.walk(loc)
    for i in dir:
        if can_iterate(i):
            for ii in i:
                if can_iterate(ii):
                    for iii in ii:
                        if can_iterate(iii):
                            for iv in iii:
                                if root_file(iv):
                                    break
                                f.write(iv+'\n')
                                # print(iv)
                        else:
                            try:
                                if root_file(iii):
                                    break
                                f.write(iii+'\n')
                                # print(iii)
                            except UnicodeEncodeError:
                                pass
                else:
                    if root_file(ii):
                        break
                    f.write(ii+'\n')
                    # print(ii)
        else:
            if root_file(i):
                break
            f.write(i+'\n')
            # print(i)


drive_iteration("D:")
drive_iteration('E:')
drive_iteration('C:')

print(r'saket \n saket')
