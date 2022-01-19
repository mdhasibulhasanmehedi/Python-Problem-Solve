s = str(input())
d = {
    'letters': 0,
    'digits': 0
}
for x in s:
    if x.isdigit():
        d['digits'] += 1
    elif x.isalpha():  # isalpha identify characters
        d['letters'] += 1
    else:
        pass
print("Letters:", d['letters'])
print("Digits:", d['digits'])
