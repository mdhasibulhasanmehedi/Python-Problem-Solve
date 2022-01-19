lines = []
while True:
    s = str(input())
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print(sentence)
