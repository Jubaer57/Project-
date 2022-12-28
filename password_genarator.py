import random




numbers = ['0','1','2','3','4' '5','6','7','8','9'] 
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special_char = ['@','#','&','*','!','?','(',')','$','~']
number_n = int(input("How many numbers you want in your password? : "))

letter_n = int(input("How many letters you want in your password? : "))

special_char_n= int(input("How many special charectar you want in your password? : "))
our_pass =[]
for char in range(1,number_n+1):
    our_pass += random.choice(numbers)

for char in range(1,letter_n+1):
    our_pass += random.choice(letter)

for char in range(1,special_char_n+1):
    our_pass += random.choice(special_char)
    
    
random.shuffle(our_pass)
password = ' '
for char in (our_pass):
    password += char


print(f"Your genarated password is{password}")



