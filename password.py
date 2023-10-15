import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=[0,1,2,3,4,5,6,7,8,9]
symbols=['!','@','#','$','%','^','&','(',')','+']
print("welcome to the password generator:")
nr_letters=int(input("enter how many letters you want to enter:\n"))
nr_numbers=int(input(f"enter how many numbers you want:\n"))
nr_symbols=int(input(f"how many symblos you want to enter:\n"))
# password=""
# for char in range(1,nr_letters+1):
#    password+= random.choice(letters)
   

# for char in range(1,nr_numbers+1):
#     password+=str(random.choice(numbers))
# for char in range(1,nr_symbols+1):
#     password+=random.choice(symbols)
# print(password)
    
password_list=[]
for char in range(1,nr_letters+1):
   password_list+= random.choice(letters)
   

for char in range(1,nr_numbers+1):
    password_list+=str(random.choice(numbers))
for char in range(1,nr_symbols+1):
    password_list+=random.choice(symbols)
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for char in password_list:
    password+=char
print(f"your password is {password}")
    



         
         
