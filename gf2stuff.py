from GF2 import one

#zz = {'a':[one,one,0,0,0,0,0],'d':[0,0,0,one,one,0,0],'b':[0,one,one,0,0,0,0],'e':[0,0,0,0,one,one,0],'c':[0,0,one,one,0,0,0],'f':[0,0,0,0,0,one,one]}

zz = {'a':[one,one,one,0,0,0,0],'d':[0,0,0,one,one,one,0],'b':[0,one,one,one,0,0,0],'e':[0,0,0,0,one,one,one],'c':[0,0,one,one,one,0,0],'f':[0,0,0,0,0,one,one]}

#u = [0,0,one,0,0,one,0]
u = [0,one,0,0,0,one,0]

result = set()

for a in zz.keys():
    for b in zz.keys():
        if [zz[a][i]+zz[b][i] for i in range(7)] == u:
            result.add(a+b)
        for c in zz.keys():
            if [zz[a][i]+zz[b][i]+zz[c][i] for i in range(7)] == u:
                result.add(a+b+c)
            for d in zz.keys():
                if [zz[a][i]+zz[b][i]+zz[c][i]+zz[d][i] for i in range(7)] == u:
                    result.add(a+b+c+d)
                for e in zz.keys():
                    if [zz[a][i]+zz[b][i]+zz[c][i]+zz[d][i]+zz[e][i] for i in range(7)] == u:
                        result.add(a+b+c+d+e)
                    for f in zz.keys():
                        if [zz[a][i]+zz[b][i]+zz[c][i]+zz[d][i]+zz[e][i]+zz[f][i] for i in range(7)] == u:
                            result.add(a+b+c+d+e+f)                        