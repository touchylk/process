# -*- coding: utf-8 -*-
from __future__ import print_function
f1='/home/e813/process/wg.txt'
f2 = '/home/e813/process/dizhi.txt'
with open(f1, 'r') as f:
    image_index = [x.strip() for x in f.readlines()]
for i in image_index:
    print(i)
    if i[-3:] != 'zip':
        fullname=i+'/'+i+'_sync.zip'
    else:
        fullname=i
    with open(f2, 'a') as f22:
        f22.writelines('http://kitti.is.tue.mpg.de/kitti/raw_data/'+fullname+'\n\n')

