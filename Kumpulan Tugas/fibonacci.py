class Fibonacci:
    def fibo(self, x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return self.fibo(x-1) + self.fibo(x-2)

f = Fibonacci()

for i in range(14):
    print (f.fibo(i))