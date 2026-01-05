import os

def check_login(username, password):
    expected_user = os.getenv("APP_USER", "admin")
    expected_pass = os.getenv("APP_PASSWORD", "secret")
    if username == expected_user and password == expected_pass:
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
