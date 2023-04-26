import sys 

def LCMS(a, b):
    v=[]
    k=[]
    for i in a:
        v.append(int(i, 16))
    for i in b:
        k.append(int(i, 16))
    
    v_i = {}
    for i, elem in enumerate(v):
        if elem not in v_i:
            v_i[elem] = []
        v_i[elem].append(i)

    lis = [0] * len(v)

    for elem in k:
        if elem in v_i:
            for i in v_i[elem]:
                lis[i] = 1
                for j in range(i):
                    if v[j] < elem:
                        lis[i] = max(lis[i], lis[j] + 1)

    lds = [0] * len(v)

    for elem in reversed(k):
        if elem in v_i:
            for i in v_i[elem]:
                lds[i] = 1
                for j in range(i+1, len(v)):
                    if v[j] < elem:
                        lds[i] = max(lds[i], lds[j] + 1)

    lcms = 0

    for i in range(len(v)):
        if lis[i] > 1 and lds[i] > 1:
            lcms = max(lcms, lis[i] + lds[i] - 1)
    
    return lcms
