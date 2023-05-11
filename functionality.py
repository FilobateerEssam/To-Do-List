import os
import pickle
import datetime

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

    while True:
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


class Task:
    def __init__(self, name_With_description, deadline=None):
        self.name = name_With_description
        self.create_time = datetime.datetime.now()
        self.deadline = deadline
        self.completed = False

    def complete(self):
        self.completed = True


import os
import pickle
import datetime

def login():
    username = input("username: ")
    password = input("Password: ")
    # Load user data from Users file using pickle
    try:
        with open("Users.txt", "rb") as f:
            while True:
                try:
                    user = pickle.load(f)
                    # Check if username and password match
                    if user["username"] == username and user["password"] == password:
                        print("Login successful!")
                        while True:
                            print("Please choose a number:")
                            print("1 - Read tasks")
                            print("2 - Add new task")
                            print("3 - Quit")
                            print()
                            choice = input()
                            if choice == "1":
                                new_tasks = read_tasks(user['username'], 'new_task')
                                completed_tasks = read_tasks(user['username'], 'completed_tasks')
                                if not new_tasks and not completed_tasks:
                                    print("No tasks found.")
                                else:
                                    print("New tasks:")
                                    for task in new_tasks:
                                        print(task)
                                    print("Completed tasks:")
                                    for task in completed_tasks:
                                        print(task)
                            elif choice == "2":
                                name_With_description = input("Enter Task : ")
                                deadline_choice = input("Do you want to add a deadline for this task? (Y/N): ")
                                if deadline_choice.upper() == "Y":
                                    deadline = input("Deadline (yyyy-mm-dd): ")
                                    try:
                                        deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d")
                                    except ValueError:
                                        print("Invalid date format!")
                                        continue
                                    task = Task(name_With_description, deadline)
                                else:
                                    task = Task(name_With_description)
                                # Save the new task to file using pickle
                                try:
                                    with open(f"{username}/new_task.txt", "ab") as f:
                                        pickle.dump(task, f)
                                        print("Task added successfully!")
                                except Exception as e:
                                    print(f"Error adding task: {e}")
                            elif choice == "3":
                                return [], []
                            else:
                                print("Please choose a valid number")
                except EOFError:
                    break
    except FileNotFoundError:
        print("No users found.")
        return
    # If no matching username and password found
    print("Invalid username or password.")

def add_task(username, task_name, deadline):
    task = Task(task_name, deadline)
    try:
        with open(f"{username}/new_task.txt", "ab") as f:
            pickle.dump(task, f)
    except Exception as e:
        print(f"Error writing task to file: {e}")
        return


def read_tasks(username, file_name):
    tasks = []
    try:
        with open(f"{username}/{file_name}.txt", "rb") as f:
            while True:
                try:
                    task = pickle.load(f)
                    tasks.append(task)
                except EOFError:
                    break
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error reading tasks from file: {e}")
    return tasks
