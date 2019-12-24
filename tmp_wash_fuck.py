import sys
import os

t = sys.argv
i = t[1]
t = t[2]

L = []

for parent, dirnames, filenames in os.walk(t):
    for filename in filenames:
        name = os.path.join(parent, filename)

        if not name[-3: len(name)] == 'txt':
            continue

        L.append(name)

L.sort()

i = int(i)

os.system('./tmp_wash ' + L[i] + ' ' + 'misc_washed/' + L[i])