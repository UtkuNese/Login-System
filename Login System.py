user = "root"
password = "12345"

while True:
    username = input("Enter your username: ")
    entered_password = input("Enter your password: ")
    
    # Both correct
    if username == user and entered_password == password:
        print("Welcome")
        break
    # Correct username, incorrect password
    elif username == user and entered_password != password:
        print("Incorrect password\n")
    # Correct password, incorrect username
    elif username != user and entered_password == password:
        print("Incorrect username\n")
    # Both incorrect
    else:
        print("Incorrect username and password\n")