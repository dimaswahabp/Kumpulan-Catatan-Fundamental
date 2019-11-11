days = {
    'Senin':'Monday','Selasa':'Tuesday','Rabu':'Wednesday','Kamis':'Thursday','Jumat':'Friday','Sabtu':'Saturday',
    'Minggu':'Sunday'
}

hari = list(days)
day = list(days.values())

x = input('Ketik nama hari (ENG/IDN)')

if x.capitalize() in hari:
    engHari = day[hari.index(x.capitalize())]
    print(f'Bhs Inggris {x.capitalize()} adalah{engHari}')
else:
    idDay = hari[day.index(x.capitalize())]
    print (f'Bhs Indonesia {x.capitalize()} adalah {idDay}')
