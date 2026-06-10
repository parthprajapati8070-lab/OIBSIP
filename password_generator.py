import random
import string

print("------ Password Generator ------")

password_length = int(input("Enter password length: "))

if password_length < 4:
    print("Password length should be at least 4.")
    exit()

print("\nInclude special characters?")
print("1 -> Yes")
print("2 -> No")

choice = int(input("Enter your choice: "))

# character collections
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

if choice == 1:
    all_characters = letters + numbers + symbols

elif choice == 2:
    all_characters = letters + numbers

else:
    print("Invalid choice.")
    exit()

generated_password = ""

for i in range(password_length):
    generated_password += random.choice(all_characters)

print("\nGenerating password......")

print("\nYour Generated Password is:")
print(generated_password)