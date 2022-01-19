class sample:
    @staticmethod
    def even(n):
       li=[i for i in range(n)  if i%2==0]
       return li

n=input("Enter any number:")
n=int(n)
print(sample.even(n))