from glob import glob
import os
rootpath = './Code'
filelist = glob(f'{rootpath}/*.*.py')
for filepath in filelist:
    filename = os.path.basename(filepath)
    i = 0
    for c in filename:
        i += 1
        if c == '.':
            break
    number = int(filename[:i-1])
    filename = filename[i:]
    newpath = '{}/{:0>4d}.{}'.format(rootpath,number,filename)
    os.rename(filepath,newpath)