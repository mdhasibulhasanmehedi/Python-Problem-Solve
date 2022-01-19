def fun(n):
    i=0
    while(i<=n):  
       i+=1
       if(i%7==0):
           yield i    
    
         
# result=fun()
#  print(fun().__next__())

n=int(input())
for x in fun(n):
   print(x)



