#list
x = [
    (1,['a','b','c'], 3),
    (4,5,6)
]
print(x)

x = [
    (1,['a','b','c'], 3),
    (4,5,6)
]
x[0][1][2] = 'Andi' 
print(x)

x = [
    (1,['a','b','c'], 3),
    (4,5,6)
]
x[0][1][2] = 'Andi'
x[0][1].append('d')
print(x)

x = [
    (1,['a','b','c'], 3),
    (4,5,6)
]
x[0][1][2] = 'Andi'
x[0][1].append('d')

x=tuple(x)
x[0][1][2] = 'Budi'
print(x)

#set
z = {1, 2, 3, 1, 2, 3}
print(type(z))
# set tidak memilik index

#add
z.add('a')
z.add(('c', 'd', 'e'))
print(z)

# set hanya bisa menambahkan immutable value
z.add([1,2,3])
print(z)
# maka akan error. karena list adalah mutable

# remove(), discard() and pop()
# remove dan discard fungsinya hampir sama.
# bedanya jika ingin menghapus element yang tidak ada, remove() akan mengeluarkan error
# sedangkan discard() tidak menampilkan error.
# pop() menghapus element secara random

z.remove(4) # ini akan error
z.discard(4) # ini tidak akan error
z.pop() # menghapus element entah urutan yang mana
z

# clear
z_copy = z.copy()
z_copy.clear()
z_copy

#irisan (intersection() / + ) dan selisih (difference() / - )
a_list = list('abcde')
b_list = list('bcfgh')
print(a_list)
print(b_list)

a_set = set(a_list)
b_set = set(b_list)
print(a_set)
print(b_set)

# for loops
z_list = list(z)
print(z_list)
print(z_list[0])

new_list = []
for i in list(z):
    new_list.append(i)
new_list