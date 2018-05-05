import string

def From10to(number, b):
    if number>=0 and 1<b<11:
        converted = ''
        while number > 0:
            converted=str((number%b))+converted
            number //= b
        return converted

#.......
def FromOtherTo10(number, b):
    if 1<b<11:
        return int(number, b)

#.......
def Convert(number, a, b):
    return From10to(FromOtherTo10(number, a), b)

#.....MAIN...................................
number=str(input('Adjon meg egy számot!'))
b1=int(input('Adja meg az alap számrendszert! '))
b2=int(input('Adja meg a cél számrendszert! '))
print(Convert(number,b1,b2))
