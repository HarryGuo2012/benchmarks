import os
import sys
from shutil import copyfile

f = open('big_list.txt', 'r')

lines = f.readlines()
haha = set()

for line in lines:
    haha.add(line[0 : len(line) - 1] + '.txt')

if not os.path.isdir('big_temp'):
    os.mkdir('big_temp')

for root, dire, filenames in os.walk('.', topdown=False):
    for filename in filenames:
        if filename in haha:
            copyfile(os.path.join(root, filename), os.path.join('big_temp', filename))

