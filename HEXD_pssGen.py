import random
password = []
# Very simple password generator
x = input("How many characters would you like to include?")
def gen_pass():
    for i in range(1,int(x)):
        v = random.choice("ABCDEFG1234567890")
        password.append(v)
    return"".join(password)
    

print(gen_pass())
input("Enter to exit... ")
