def square(n):
     for x in range(1,n+1):
          x=x**2
          yield x

n=int(input())
for result in square(n):
     print(result)
