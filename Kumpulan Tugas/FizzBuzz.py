
def fizzbuzz(num) :
    for i in range(1,num+1) :
        if (i % 15 == 0) :
            print('FizzBuzz')
        elif (i % 3 == 0):
            print('Fizz')
        elif(i % 5 == 0):
            print('Buzz')
        else:
            print(i)

fizzbuzz(200)

for i in range(1,11):
    if i % 2 == 0:
        print('wow!')
    else:
        print(i)