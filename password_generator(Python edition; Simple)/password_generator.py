import string #Used for acquiring the various symbols, letters, and numbers
import random #Used to generate a random password

def generate_weak_password():
    chars = list(string.ascii_letters) #This is the variable that contains all the usable letters/numbers/characters for the password. Here, chars only contains letters. Depending on the user's choice, the variable will change
    password_length = int(input("Enter how long you want your password to be: "))
    random.shuffle(chars)
    password = []
    for i in range(password_length):
        password.append(random.choice(chars))
    random.shuffle(password)
    password = "".join(password)
    print("Here is your password: " + password)

def generate_strong_password():
    chars = list(string.ascii_letters + string.digits) #chars contains letters and numbers, but not special characters
    password_length = int(input("Enter how long you want your password to be "))
    random.shuffle(chars)
    password = []
    for i in range(password_length):
        password.append(random.choice(chars))
    random.shuffle(password)
    password = "".join(password)
    print("Here is your password: " + password)

def generate_vstrong_password():
    chars = list(string.ascii_letters + string.digits + string.punctuation) #chars contains letters, numbers, and special characters. Hopefully, it'll make a great password!
    password_length = int(input("Enter how long you want your password to be "))
    random.shuffle(chars)
    password = []
    for i in range(password_length):
        password.append(random.choice(chars))
    random.shuffle(password)
    password = "".join(password)
    print("Here is your password: " + password)

def generate_surprise_password():
    chars = list(string.ascii_letters + string.digits + string.punctuation) #chars is the same as the above function...
    password_length = random.randint(1, 100)
    random.shuffle(chars)
    password = []
    for i in range(password_length):
        password.append(random.choice(chars))
    random.shuffle(password)
    password = "".join(password)
    print("Here is your password. I hope you're surprised!: " + password)

first_option = input("Would you like to generate a password? (Yes/No): ")
if(first_option == "Yes") or (first_option == "yes"):
    generator_option = input("What kind of password do you want? (Weak/Strong/Very Strong/Surprise Me): ")
    if(generator_option == "Weak") or (generator_option == "weak"):
        generate_weak_password()
    elif(generator_option == "Strong") or (generator_option == "strong"):
        generate_strong_password()
    elif(generator_option == "Very Strong") or (generator_option == "very strong"):
        generate_vstrong_password()
    elif(generator_option == "Surprise Me") or (generator_option == "surprise me"):
        generate_surprise_password()
    else:
        print("Invalid input. Please try again")
        quit()
elif(first_option == "No" or "N"):
    print("Goodbye")
    quit()
else:
    print("Invalid input. The program is case sensitive. Please try again")
    quit()