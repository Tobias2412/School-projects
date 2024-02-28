correct_password = "password123"

while True:
    user_password = input("Enter the password:")
    if user_password == correct_password:
        print("Access granted. Welcome!")
    else:
        print("Incorrect password. Try again")
