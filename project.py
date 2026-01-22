password = input("Enter your password: ")

letters = False
numbers = False
symbols = False

for ch in password:
    if ch.isalpha():
        letters = True
    elif ch.isdigit():
        numbers = True
    else:
        symbols = True

if len(password) < 6:
    print("Weak password (too short)")
elif letters and numbers and symbols:
    print("Strong password")
else:
    print("Medium password")
