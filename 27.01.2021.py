with open('lista haotica a catalogului clasa X-A','r')
    a=str(f.readline()).split(',')
    a.sort()
 with open('lista haotica a catalogului clasa X-A','w')
 as f:
    for x in a:
        f.write(str(x))