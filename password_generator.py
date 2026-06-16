import random
import string
n=int(input("Enter Password length"))
ch=string.ascii_letters+string.digits+string.punctuation
psswd=""
for i in range(n):
    p=random.choice(ch)
    psswd=psswd+p
print("Generated password",psswd)


