li=[]
item=[x for x in str(input()).split(',')]

for x in item:
    r=int(x,2)#(string,base)--convert string to decimal
    if(r%5==0):
     print(x)      

# 0100,0011,1010,1001
