import random

special_characters = ['!', '@', '#', '$', '&', '-', '_', '=', '+', '?']

n=int(input("Enter the password's length:"))
password=""
for i in range(n):
    choice=random.randint(1,4)
    if choice==1:
        password+=chr(random.randint(65,90))
    elif choice==2:
        password+=chr(random.randint(97,122))
    elif choice==3:
        password+=str(random.randint(0,9))
    else:
        password+=special_characters[random.randint(0,len(special_characters)-1)]

print(password)
