fname = input('Enter file:')
if len(fname) < 1 : fname = 'txt.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1


tmp = list()
for k, v in di.items():
    newTup = (v, k)
    tmp.append(newTup)
    
tmp = sorted(tmp, reverse=True)
print('Sorted', tmp[2:5])

for v,k in tmp[2:10]:
    print(k ,v)
