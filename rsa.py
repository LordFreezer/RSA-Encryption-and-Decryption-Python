# Recursion Based
def gcd(a, b):
    global x, y
    if (b == 0):
        x=1
        y=0
        return a 
    greatest_common_divisor = gcd(b, a % b)
    x1 = x 
    y1 = y 
    
    x = y1
    y = x1 - (a // b) * y1 # // divides and returns floor
    print("a="+str(a)+" b="+str(b)+" x="+str(x)+" y="+str(y))
    return greatest_common_divisor

def modInverse (a, m):
    greatest_common_divisor = gcd(a, m)
    if(greatest_common_divisor != 1):
        print("Mod Inverse does not exist")
        return -1
    else: 
        inv = (x % m + m) % m 
        return inv

def encrypt(message, public_key):
    p, n = public_key
    return message**p % n
    
def decrypt(message, n, private_key):
    d = private_key
    return message**private_key % n

def euler_totient(p, q):
    return (p-1)*(q-1)
p=7
q=11
e=7
M=8
n = p * q
public_key = e, n
phi_n=euler_totient(p, q)
private_key = modInverse(e, phi_n)
C = encrypt(M, public_key)
decryped_m = decrypt(C, n, private_key)

print("Given p="+str(p)+" and q="+str(q)+" and e="+str(e)+" and M="+str(M))
print("private key: "+str(private_key))
print("public key: "+str(public_key))
print("Encrypted message: "+str(C))
print("Decrypted message: "+str(decryped_m))
