
class sample:
    @staticmethod
    def result(n, sum):
        for i in range(1, n+1):
            sum += float(i/(i+1))
        return sum


cin = int(input('input any number:'))
print(round(sample.result(cin, sum=0.0), 2))  # round(sum,2) --3.550000=3.55
