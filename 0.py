
# # # nama =  open('dimas.txt','r')
# # # x = nama.read().split(",")
# # # '''
# # # for i in x: 
# # #     print(i)
# # # '''
# # # koceng = open('dimasw.csv','w')
# # # for i in x: 
# # #     koceng.write

# # nama = open('dimasw.csv','r')
# # x = nama.read().split("\n")
# # y = []
# # for i in x:
# #     i = i.split(",")
# #     y.append(i)
# # listDasar = y[0]
# # c = []
# # for z in range(len(y)-1):
# #     i = dict(zip(listDasar,(y[1:][z])))
# #     c.append(i)

# # print(c)
# import csv
# with open("dimasw.csv","r") as x:
#     baca = csv.reader(x)
#     e = (list(baca))
# listBaru =e[0]
# c = []
# for z in range(len(e)-1):
#     i = dict(zip(listBaru,(e[1:][z])))
#     c.append(i)
# print(c)
'''
import csv
c = []
with open("dimasw.csv","r") as x:
    baca = csv.DictReader(x)
    print(list(baca))
'''
import csv
data = [
    {"nama" : "andi", "usia ": 22, "kota":"jakarta"},
    {"nama" : "luna", "usia ": 24, "kota":"solo"},
    {"nama" : "aiman", "usia ": 23, "kota":"semarang"}
]

with open("mawuteng.csv","w",newline="") as x:
    kolom = ["nama", "usia ", "kota"]
    a = csv.DictWriter(x, fieldnames=kolom, delimiter=",")
    a.writeheader()
    a.writerows(data)
