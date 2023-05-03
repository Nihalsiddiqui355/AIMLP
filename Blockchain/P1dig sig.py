#pip install pycryptodome
from Crypto.PublicKey import RSA
from hashlib import sha512
#generating 1024 bits RSA keyPair
keyPair = RSA.generate(bits=1024)
#public key (n,e)
print(f"\nPublic Key: (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
#private key (n,d)
print(f"\nPrivate Key: (n={hex(keyPair.n)}, e={hex(keyPair.d)})")
#Generate RSA Signature using private key(n,d)
msg = "Welcome to K.C. College"
print("\nMessage: ",msg)
hash=int.from_bytes(sha512(msg.encode('utf-8')).digest(), byteorder='big')
#modular exponentiation = pow(x,y,n)
signature = pow(hash, keyPair.d, keyPair.n)
#RSA verify Signature using Public Key(n,e)
msg = "Welcome to K.C. College"
print("Verifying for: ",msg)
hash=int.from_bytes(sha512(msg.encode('utf-8')).digest(), byteorder='big')
hashfromsignature= pow(signature, keyPair.e, keyPair.n)
if hash==hashfromsignature:
 print("Signature Valid")
else:
 print("Signature Invalid! Message tampered")
#RSA verify Signature using Public Key(n,e) with tampered msg
msg = "Welcome to K.C. College Churchgate"
print("Verifying for: ",msg)
hash=int.from_bytes(sha512(msg.encode('utf-8')).digest(), byteorder='big')
hashfromsignature= pow(signature, keyPair.e, keyPair.n)
if hash==hashfromsignature:
 print("Signature Valid")
else:
 print("Signature Invalid! Message tampered")
