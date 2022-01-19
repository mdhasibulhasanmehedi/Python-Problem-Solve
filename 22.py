# d={}
# s=str(input())
# for word in s.split(' '):
#     d[word]=d.get(word,0)+1

# for key in sorted(d):
#     print("{}:{}".format(key,d[key]))

d = dict()
for word in str(input()).split(' '):
    d[word] = d.get(word, 0)+1
words = d.keys()

words = sorted(words)

for index in words:
    print("{}:{}".format(index, d[index]))
