#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


# Way 1

# random_letters = random.choices(letters, k = nr_letters)
# random_numbers = random.choices(numbers, k = nr_numbers)
# random_symbols = random.choices(symbols, k = nr_symbols)

# print("".join(random_letters) + "".join(random_numbers) + "".join(random_symbols))

# Way 2

# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)

# for char in range(0, nr_numbers):
#     password += random.choice(numbers)

# for char in range(1, nr_symbols):
#     password += random.choice(symbols)

# print(password)

# Way 3

password = []
random_password = ""
for char in range(0, nr_letters):
    password.append(random.choice(letters))

for char in range(0, nr_numbers):
    password.append(random.choice(numbers))

for char in range(0, nr_symbols):
    password.append(random.choice(symbols))

# print(password)
# random.shuffle(password)
# print(password)

for chart in password:
    random_password += random.choice(chart)

print(random_password)