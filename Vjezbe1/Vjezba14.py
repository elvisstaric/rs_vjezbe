#1
def isPrime(a):
    cnt=0
    b=a
    while b>0:
        if(a%b==0):
            cnt=cnt+1
        b=b-1
    if cnt>2:
        return False
    else:
        return True

print(isPrime(7))
print(isPrime(10))

#2
def primes_in_range(a,b):
    lista_prime=list()
    for i in range(a,b):
        if isPrime(i) is True:
            lista_prime.append(i)
    return lista_prime

print(primes_in_range(1,10))