s=str(input())
d={
 'upper':0,
  'lower':0   
}
for x in s:
   if x.isupper():
     d['upper']+=1
   elif x.islower():
        d['lower']+=1
   else:
    pass

print('UPPER CASE',d['upper'])
print('LOWER CASE',d['lower'])