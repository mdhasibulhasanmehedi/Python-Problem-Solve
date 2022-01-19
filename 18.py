s=str(input())
li=[x for x in s.split(',')]
for s in li:
 lower=upper=digit=char=0
 if(len(s)>=6 and len(s)<=12):
   for x in s:
    if(x.islower()):lower+=1   
    elif(x.isupper()):upper+=1  
    elif(x.isdigit()):digit+=1 
    elif(x=='$' or x=='#' or x=='@'):
     char+=1  
    else:pass    

 if(lower>=1 and upper>=1 and digit>=1 and char>=1):
     print(s)
