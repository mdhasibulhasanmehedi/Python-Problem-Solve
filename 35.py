# def fuc(n):
#     d={}
#     for i in range(1,n+1):
#         d[i]=i**2
#     for(x,y)in d.items():
#         yield y    

# for ans in fuc(20):
#     print(ans,end=" ")  

def print_dict(n):
    d=dict()
    for i in range(1,n):
         d[i]=i**2
    for(k,v) in d.items():
         print(v,end=' ')     

n=int(input())
print_dict(n)
