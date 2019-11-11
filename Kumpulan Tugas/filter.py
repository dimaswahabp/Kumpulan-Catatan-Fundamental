x = range(11)
def kurang_lima(a):
    if a < 5:
        return False
    else:
        return True
    
y = filter(kurang_lima, x)
print(list(y))

x = [1,2,3,4,5]
y = [1,2,6,7,8]

z = filter(lambda a: a in x, y)
print(list(z))