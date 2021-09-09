import random
chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$^&*'
number = input('N. of password-?')
number = int(number)
length = input('password length-?')
length = int(length)
for p in range(number):
    password = ''
    for c in range(length):
        password+=random.choice(chars)
    print(password)
    
