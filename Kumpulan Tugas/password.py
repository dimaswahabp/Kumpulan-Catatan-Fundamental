password = '12345'
inputuser = ''
jumlahinput = 0
batasinput = 5
lebih = False



while inputuser != password and not lebih:
    if jumlahinput < batasinput:
        inputuser = input(f'percobaan ke-{jumlahinput+1} masukin Password:')
        jumlahinput += 1
    else:
        lebih = True

if lebih:
    print('Kesempatan Habis, Yaude lah yaa')
else:
    print('Your Password is Correct!')