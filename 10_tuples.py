# las tuplas son immutables
# tuples arent immutabales

(x, y) = (4, 'fred')
print(y)

tmp = list()
d = {'a': 10, 'b': 1, 'c': 22}
print(d)
# t = sorted(d.items())
# for k, v in t:
#     tmp.append( (v,k) )

# print(tmp)

# tmp = sorted(tmp, reverse=True)
# print(tmp)

print( sorted( [ (v,k) for k,v in d.items()]))