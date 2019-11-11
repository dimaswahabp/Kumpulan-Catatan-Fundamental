import math
hari = ['mon','tue','wed','thur','fri','sat','sun']

sekarang hari Sekarang hari 'wed', hari apakah 100 hari lagi?

# now= 'wed'; brpHari = 100;

now = 'mon'
brpHari = 5
iNow = hari.index(now)
sisaHari = brpHari % len(hari)
hariYGdicari = hari[(iNow +sisaHari) % 7]
print(hariYGdicari)