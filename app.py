import os

def check_login(username, password):
    if username == "admin" and password == "123456":
        print("Login Successful!")
        return True

    else:
        print("Login Failed!")
        return False

def main():
    print("--- DevSecOps Simple App ---")
    user = input("Enter username: ")
    pw = input("Enter password: ")
    check_login(user, pw)

if __name__ == "__main__":
    main()
