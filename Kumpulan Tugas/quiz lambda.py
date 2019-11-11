num_list = list(range(1,101))
mantap = reduce(lambda x,y:x+y, map(lambda x:x*2, filter(lambda x:x%2==0, num_list)))
print(num_list)

num_list = list(range(1,101))
even = [i%2==0 for i in num_list]
even_2 = [i*2 for i in even]
sum_even = sum(even_2)
print(even)
print(even_2)
sum_even

