result=0
while True:
   
    s=str(input())
    if not s:
        break
    values=s.split(' ')
    if(values[0]=='D'):
       result+=int(values[1])  
    elif(values[0]=='W'):
        result-=int(values[1])
    else:
        pass  

print(result)    

# D 300 D 300 W 200 D 100 