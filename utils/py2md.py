'''
Description: 
Autor: Au3C2
Date: 2021-03-26 10:22:10
LastEditors: Au3C2
LastEditTime: 2021-03-26 10:38:18
'''
import os
from glob import glob

filelist = glob('Code/*/*.py')

for filepath in filelist:
    newpath = filepath.replace('.py','.md')
    os.rename(filepath,newpath)
    with open(newpath,'r',encoding='utf8') as fp:
        data = fp.readlines()
    data.insert(0,'```python\n')
    data.append('\n```\n')
    with open(newpath,'w',encoding='utf8') as fp:
        fp.writelines(data)