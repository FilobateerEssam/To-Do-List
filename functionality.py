import os
import pickle

def start():
    print("------------------------------------------------------------")
    print("Welcome to your ToDO List")
    print("------------------------------------------------------------")
    print("Please choose a number:")
    print("1 - Login")
    print("2- Register")
    print("3- Quit")
    print()

    choice = input()

    while 1:
        if choice == '1':
            return login()
            # break
        elif choice == '2':
            register()
            return [], []
        elif choice == '3':
            return
        else:
            choice = input("Please choose a valid number\n")

def register():
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")
    # Check if username already exists in File Users
    try:
        with open("Users.txt", "rb") as f:
            while True:
                try:
                    user = pickle.load(f)
                    if user["username"] == username:
                        print("Username already exists!")
                        return
                except EOFError:
                    break
    except FileNotFoundError:
        pass

    # Create a new user object
    user = {"username": username, "email": email, "password": password}

    # Write user data in Users file using pickle
    try:
        with open("Users.txt", "ab") as f:
            pickle.dump(user, f)
    except Exception as e:
        print(f"Error writing to Users file: {e}")
        return

    # Create Folder with UserName
    try:
        os.mkdir(username)
    except Exception as e:
        print(f"Error creating User Folder: {e}")
        return

    # Create new task file
    try:
        with open(f"{username}/new_task.txt", "w") as f:
            pass
    except Exception as e:
        print(f"Error creating new_task.txt: {e}")
        return

    # Create completed file
    try:
        with open(f"{username}/completed_tasks.txt", "w") as f:
            pass
    except Exception as e:
        print(f"Error creating completed.txt: {e}")
        return

    print("Registration successful!")

def login():
    email = input("Email: ")
    password = input("Password: ")
    # Load user data from Users file using pickle
    try:
        with open("Users.txt", "rb") as f:
            while True:
                try:
                    user = pickle.load(f)
                    # Check if username and password match
                    if user["email"] == email and user["password"] == password:
                        print("Login successful!")
                        new_tasks = read_tasks(user['username'],'new_task')
                        completed_tasks = read_tasks(user['username'],'completed_tasks')
                        return new_tasks, completed_tasks
                except EOFError:
                    break
    except FileNotFoundError:
        print("No users found.")
        return

    # If no matching username and password found
    print("Invalid email or password.")

def read_tasks(username, fileName):
    tasks = []
    try:
        with open(f"{username}/{fileName}.txt", "r") as f:
            for line in f:
                tasks.append(line.strip())
    except Exception as e:
        print(f"Error reading new_task.txt: {e}")
    return tasks
