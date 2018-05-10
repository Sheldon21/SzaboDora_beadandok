
def prime(szam):
    for i in range(2,szam):
        if(szam%i == 0):
            return False
    return True

#.....MAIN............
i = 0
number = 2
while i != 10001:
    if prime(number):
        i = i + 1
#        print(i)
    number += 1

print(number)

