x = 'malam'

def palindrome(kata) :
    if kata == kata[::-1] :
        return True
    else:
        return False
print(palindrome(x))


def palindrome2(kata):
    for i in range(round(len(kata)/2)):
        palindromekah = False
        if kata[i] == kata[len(kata)-1-i]:
            palindromekah = True
        else:
            palindromekah = False
            break
        return palindromekah

    print(palindrome2('Katak'))
    print(palindrome2('kokok'))