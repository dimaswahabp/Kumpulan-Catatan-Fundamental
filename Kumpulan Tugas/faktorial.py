def faktorial2(x):
    if x <= 2:
        return x
    else:
        return x * faktorial2(x-1)
    
print (faktorial2())
    
# f(4) = 4*8 = 32
# f(3) = 3*2 = 6