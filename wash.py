import os
import sys
import re

def unzip(dom, name):
    fileName = os.path.join(dom, name + '.zip')

    os.system('unzip -o ' + fileName)

def deal_file(dom, name):
    if os.path.isfile(name + '.edges'):
        print('It is edges format')
        deal_with_edgelist(dom, name)
        return True
    if os.path.isfile(name + '.mtx'):
        print('It is mtx format')
        deal_with_mtx(dom, name)
        return True
    return False

def deal_with_mtx(dom, name):
    print('Converting mtx to txt...')
    fileName = name + '.mtx'
    f = open(fileName, 'r')

    result = []

    cnt = 0

    for line in f.readlines():
        if line[0] == '%':
            continue
        cnt = cnt + 1
        haha = line
        if cnt == 1:
            haha = re.findall('\d* (\d* \d*)', line)
            haha = haha[0]
            result.append(haha)
        else:
            xixi = haha.split()
            if len(xixi) == 2:
                result.append(haha)
            else:
                result.append(xixi[0] + ' ' + xixi[1] + '\n')

    f.close()

    with open(os.path.join(dom, name + '.txt'), 'w') as fw:
        fw.write('%s' % '\n'.join(result))
    print('Converting finished')

def deal_with_edgelist(dom, name):
    print('Converting edgelist to txt...')
    fileName = name + '.edges'
    dict = {}
    se = set()
    f = open(fileName, 'r')

    result = []

    n = 0
    cnt = 0

    for line in f.readlines():
        cnt = cnt + 1

        if line[0] == '%':
            continue

        haha = re.findall('(\d{1,})', line)
        
        #print(haha)

        u = int(haha[0])
        v = int(haha[1])

        if u in dict:
            u = dict[u]
        else:
            n = n + 1
            dict[u] = n
            u = dict[u]

        if v in dict:
            v = dict[v]
        else:
            n = n + 1
            dict[v] = n
            v = dict[v]

        if u == v:
            continue

        if (u, v) in se:
            continue
        if (v, u) in se:
            continue

        se.add((u, v))

        result.append([u, v])

    f.close()
    m = len(result)

    result = [[n, m]] + result
    res = []
    for tmp in result:
        res.append(str(tmp[0]) + ' ' + str(tmp[1]))

    with open(os.path.join(dom, name + '.txt'), 'w') as fw:
        fw.write('%s' % '\n'.join(res))
    print('Converting finished')

def remove_tmp(dom, name):
    print('removing template files')
    if os.path.isfile(name + '.edges'):
        os.system('rm -rdf ' + name + '.edges')
    if os.path.isfile(name + '.mtx'):
        os.system('rm -rdf ' + name + '.mtx')
    if os.path.isfile('readme.html'):
        os.system('rm -rdf readme.html')
    if os.path.isfile('readme.txt'):
        os.system('rm -rdf readme.txt')
    if os.path.isfile(os.path.join(dom, name + '.zip')):
        os.system('rm -rdf ' + os.path.join(dom, name + '.zip'))
