vocalwords = list('aiueo')
print(vocalwords)

def changevocal(param) :
    newstring = ''
    for i in param:
        if i in vocalwords:
            i = 'o'
            newstring += i 
        else:
            newstring += i
        
    print(newstring)

changevocal(input('Masukkan Kata:').lower())
