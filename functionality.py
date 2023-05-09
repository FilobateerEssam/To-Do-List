import os
import pickle


def register(username, email, password):

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

