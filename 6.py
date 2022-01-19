import math
c,h=50,30
value=[]
s=str(input())
items=s.split(',')

for d in items:
    value.append(str(int(math.sqrt(2*c*float(d)/h))))

print(','.join(value))

# items=[x for x in str(input()).split(',')]

# for d in items:
#     value.append(str(int(math.sqrt(2*c*float(d)/h))))

# print(','.join(value))


