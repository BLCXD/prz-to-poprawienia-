# Tutaj pisz swój kod, młody padawanie ;-)
def rozklad(n):
   i = 2
    czyn = []
    
    while i*i <= n:
        while n % i == 0:
            czyn.append(i)
            n //= i
        i+=1
        
    if n > 1:
        czyn.append(n)
    return sum(czyn) - czyn[len(czyn)-1]





def fsmult(b):
    return rozklad(b)

def fnwd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
if a == b:
    print(0)

else:
    nwd = fnwd(a, b)
    nww = (a * b) // nwd
    if b > a:
        if b % a != 0:
            x = a // nwd
            c = a // x
            y = b // c
            if c * y == b:
                smult = fsmult(b)
                print(int(x + smult))

        elif b%a == 0:
            print(b // a)
    else:
        if a%b ==0:
            print(a//b)
        else:

            x = nww // a
            y = nww // b
            print(x + y)

