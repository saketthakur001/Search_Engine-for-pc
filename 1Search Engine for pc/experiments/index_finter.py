import os

dir = []
f = open("C:\index\index_data.txt", "w+")

def can_iterate(ex):
    if type(ex) == list:
        return True
    elif type(ex) == tuple:
        return True

# def et(z):
    # if can_iterate:
    #     for i in z:
    #         return i

def iterate(ex):
    for i in ex:
        return  
        
def root_file(file):
    if file[0] == "$":
        return True

def filter(num, dig):
    if num % 10000 == 0:
        print(dig)


def drive_iteration(loc):
    dir = os.walk(loc)
    num = 1
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
                                filter(num, iv)
                                num +=1
                        else:
                            try:
                                if root_file(iii):
                                    break
                                f.write(iii+'\n')
                                filter(num, iii)
                                num +=1
                            except UnicodeEncodeError:
                                pass
                else:
                    if root_file(ii):
                        break
                    f.write(ii+'\n')
                    filter(num, ii)
                    num +=1
        else:
            if root_file(i):
                break
            f.write(i+'\n')
            filter(num, i)
            num +=1
    print(num, 'files added to your index')

drive_iteration("D:")
drive_iteration('E:')
drive_iteration(r'C:\Users\saket\Desktop')
drive_iteration(r'C:\Users\saket\Music')
drive_iteration(r'C:\Users\saket\Pictures')
drive_iteration(r'C:\Users\saket\Downloads')

print('saket\nsaket')
