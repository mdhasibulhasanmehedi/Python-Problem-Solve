li= [x for x in str(input()).split(' ')]
s=set(li) #covert list to set
li=list(s) #covert set to list s
li.sort()
#print( " ".join(sorted(list(set(li))))) //three lines=1 line
print(' '.join(li))

