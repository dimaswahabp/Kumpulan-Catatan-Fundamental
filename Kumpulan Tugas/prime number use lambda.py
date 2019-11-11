num_list = list(range(0,100))
prime = list(filter(lambda x:x%11!=0 or x==11,
                    filter(lambda x:x%7!=0 or x==7,
                           filter(lambda x:x%5!=0 or x==5,
                                  filter(lambda x:x%3!=0 or x==3,
                                         filter(lambda x:x%2!=0 or x==2,
                                                filter(lambda x:x>1, num_list)))))))
print(prime)