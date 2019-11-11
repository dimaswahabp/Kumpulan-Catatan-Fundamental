p = [1, 2 ,4, 7 ,9 ,19]
q = [5, 6, 7 ,9, 12, 16,17, 19]
r = [3, 6, 8, 19]
p = set(p)
q = set(q)
r = set(r)
print(p & q)
print(q & p)
print(p &(q & r))

# frozen set = set ysng bersifat immutable
x = set ([1, 2, 3])
y = frozenset([1, 2, 3])
x.remove(2)
# y.add(2)
print(type(y))
print(len(y))


s = {0, 1, 2, 3, 4, 5, 6, 7, 8,
 9, 10}
a = {2 ,3, 5, 7}
b = {5 , 7, 9}
x = (a & b)
y = (a | b)

print(a & b)
print(b & a)
print(a & (a | b))
print(b &( a | b))
print((a | b) & (a|b))
print(x | y)