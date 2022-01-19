# s = str(input())
# dimension = [int(x) for x in s.split(',')]

# row = dimension[0]
# col = dimension[1]
# multiset = [[0 for i in range(col)]for j in range(row)]

# for i in range(row):
#     for j in range(col):
#         multiset[i][j] = i*j

# print(multiset)

dimension = [int(x) for x in (str(input())).split(',')]
row = dimension[0]
col = dimension[1]
multilist = [[0 for j in range(col)]for i in range(row)]
multilist = [[i*j for j in range(col)]for i in range(row)]
print(multilist)
for i in range(row):
    for j in range(col):
        print(multilist[i][j],end=' ')
    print()     
