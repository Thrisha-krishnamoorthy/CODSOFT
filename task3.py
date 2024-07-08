import random
import string

def generate_password(length, complexity):
    characters = ""
    if complexity >= 1:
        characters += string.ascii_lowercase
    if complexity >= 2:
        characters += string.ascii_uppercase
    if complexity >= 3:
        characters += string.digits
    if complexity >= 4:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    complexity = int(input("Enter the desired complexity of the password (1-4): "))
    password = generate_password(length, complexity)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()

