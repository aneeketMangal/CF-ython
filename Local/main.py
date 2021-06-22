
#?############################################################


def isPrime(x):
    for i in range(2, x):
        if i*i > x:
            break
        if (x % i == 0):
            return False
    return True

#?############################################################


def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p


#?############################################################

def primeFactors(n):
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            l.append(int(i))
            n = n / i
    if n > 2:
        l.append(n)
    return list(set(l))


#?############################################################

def power(x, y, p):
    res = 1
    x = x % p
    if (x == 0):
        return 0
    while (y > 0):
        if ((y & 1) == 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

#?############################################################


def sieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime


#?############################################################

def digits(n):
    c = 0
    while (n > 0):
        n //= 10
        c += 1
    return c

#?############################################################


def ceil(n, x):
    if (n % x == 0):
        return n//x
    return n//x+1

#?############################################################


def mapin():
    return map(int, input().split())

#?############################################################
def solve(dd, n):
    x = 0
    for i in range(n):
        if(dd[i] == "("):
            x+=1
        elif(dd[i] == ")"):
            x-=1
        if(x <= 0 and i!= n-1):
            return -1

    
    if(x == 0):
        return dd
    else:
        return -1
            



input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# python3 15.py<in>op
n = int(input())
l = input()
if(n&1):
    print(":(")
else:
    a = l.count("(")
    b = l.count(")")
    if(a>n//2 or b>n//2):
        print(":(")
    else:

        a = n//2-a
        b = n//2-b
        l = l.replace('?', '(', a)
        l = l.replace('?', ')')
        
        ans =solve(l, n)
        # print(ans)
        if(ans == -1):
            print(":(")
        else:
            print(l)