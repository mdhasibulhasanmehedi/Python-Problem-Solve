import math
x_axis=y_axis=0
while True: 
    lol=str(input()) #s=[up/down/left/right,values]
    if not lol:
        break
    s=lol.split(' ')
    if(s[0]=='UP'):
         y_axis+=int(s[1])
    elif(s[0]=='DOWN'):
         y_axis-=int(s[1])
    elif(s[0]=='RIGHT'):
         x_axis+=int(s[1])
    elif(s[0]=='LEFT'):
         x_axis-=int(s[1])   
    else:pass                
result= int(math.sqrt((x_axis**2)+(y_axis**2)))    
print(result)