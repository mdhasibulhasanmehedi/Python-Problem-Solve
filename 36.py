def print_dict(n):
    d=dict()
    for i in range(1,n):
         d[i]=i**2
    for(k,v) in d.items():
         yield k 

n=int(input())
values=print_dict(n)
# print(next(values))
# print(next(values))
# print(values.__next__())
for x in values:
    print(x)