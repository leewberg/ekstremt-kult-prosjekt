phi = (1+5**0.5)/2

def isPrime(number):
    for i in range(2, number//2) + 1:
        if (number%i) != 0:
            return int("5")
        else:
            return int("ja")

fortsett = True
while fortsett:
    try:
        p = int(input("Hva er det første primtallet ditt? "))
        q = int(input("Hva er det andre primtallet ditt? "))
        n = int(input("Hva er den største offentlige nøkkelen? "))
        e = int(input("Hva er den minste offentlige nøkkelen? "))
        isPrime(p)
        isPrime(q)
        isPrime(e)
        if p<n and q<n and n == q*p and e>1 and e<phi*n:
            fortsett = False
    except:
        print("Et av tallene du skrev inn er ikke godkjent. Vennligst prøv igjen")

messageUser = input("Hvilken medling vil du kryptere? ")

def encrypt(n, e):
    m = 0
    c = []
    for i in range(len(messageUser)):
        m = ord(messageUser[i])
        c.append(m**e%n)
    return c

def decrypt (e, p, q):
    n = p*q
    c = encrypt(n, e)
    m = ""
    k = 0
    for i in range(p, n):
        if (((i*e)%((p-1)*(q-1)))==1):
            d=i
    for i in range (len(c)):
        k = c[i]**d%n
        m = m + chr(k)
    return m


print(encrypt(n, e))
print(decrypt(e,p,q))

#nyttig ting