import os
import pickle
import datetime

def start():
    print("------------------------------------------------------------")
    print("Welcome to your ToDO List")
    print("------------------------------------------------------------")
    print("Please choose a number:")
    print("1- Login")
    print("2- Register")
    print("3- Quit")
    print()

    choice = input()

    while True:
        if choice == '1':
            return login()
        elif choice == '2':
            return register()
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
        with open("Users.pkl", "rb") as f:
            while True:
                try:
                    user = pickle.load(f)
                    if user["username"] == username:
                        print("Username already exists!")
                except EOFError:
                    break
    except FileNotFoundError:
        pass

    # Create a new user object
    user = {"username": username, "email": email, "password": password}

    # Write user data in Users file using pickle
    try:
        with open("Users.pkl", "ab") as f:
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
        with open(f"{username}/new_task.pkl", "wb") as f:
            pass
    except Exception as e:
        print(f"Error creating new_task.pkl: {e}")
        return

    # Create completed file
    try:
        with open(f"{username}/completed_tasks.pkl", "wb") as f:
            pass
    except Exception as e:
        print(f"Error creating completed.pkl: {e}")
        return

    print("Registration successful!")
    return User(username)

class User:
    def _init_(self,name):
        self.username = name
        self.new_tasks = []
        self.completed_tasks = []
    def fill_new_tasks(self):
        self.new_tasks = read_tasks(self.username,'new_task')
    def fill_completed_tasks(self):
        self.completed_tasks = read_tasks(self.username,'completed_tasks')

def login():
    username = input("username: ")
    password = input("Password: ")
    # Load user data from Users file using pickle
    try:
        with open("Users.pkl", "rb") as f:
            while True:
                try:
                    user = pickle.load(f)
                    # Check if username and password match
                    if user["username"] == username and user["password"] == password:
                        my_user = User(name=username)
                        my_user.fill_new_tasks()
                        my_user.fill_completed_tasks()
                        print("Login successful!")
                        return my_user

                except EOFError:
                    break
    except FileNotFoundError:
        print("No users found.")
        return start()
    # If no matching username and password found
    print("Invalid username or password.")
    return start()

def read_tasks(username, file_name):
    tasks = []
    try:
        with open(f"{username}/{file_name}.pkl", "rb") as f:
            data = pickle.load(f)
            for s in data:
                tasks.append(s)
    except FileNotFoundError:
        pass
    except EOFError:
        pass
    except Exception as e:
        print(f"Error reading tasks from file: {e}")
    return tasks

def Home(obj_user):
    while True:
        print("Please choose a number:")
        print("1 - View tasks")
        print("2 - Add new task")
        print("3 - Mark task as Completed")
        print("4 - Delete task")
        print("5 - Quit")
        print()
        choice = input()
        if choice == "1":
            view_tasks(obj_user)
        elif choice == "2":
             add_new_task(obj_user)
        elif choice == "3":
             mark_as_completed(obj_user)
        elif choice == "4":
             delete_task(obj_user)
        elif choice == "5":
            Quit(obj_user)
            return
        else:
            print("Please choose a valid number")

def view_tasks(obj_user):
    new_tasks = obj_user.new_tasks
    completed_tasks = obj_user.completed_tasks
    if not new_tasks and not completed_tasks:
        print("No tasks found.")
    else:
        print("New tasks:")
        for i,task in enumerate(new_tasks):
            print(f"{i+1}. {task}")

        print("Completed tasks:")

        for i, task in enumerate(completed_tasks):
            print(f"{i+1}. {task}")

def add_new_task(obj_user):
    name_With_description = input("Enter Task : ")
    deadline_choice = input("Do you want to add a deadline for this task? (Y/N): ")
    if deadline_choice.upper() == "Y":
        deadline = input("Deadline (yyyy-mm-dd): ")
        try:
            deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d")

        except ValueError:
            print("Invalid date format!")
            return
        obj_user.new_tasks.append(name_With_description + " Due Date :  " + str(deadline))

    else:
        obj_user.new_tasks.append(name_With_description)
def mark_as_completed(obj_user):
    view_tasks(obj_user)
    print()
    try:
        index = int(input("Enter Task Number: "))
        obj_user.completed_tasks.append(obj_user.new_tasks[index - 1])
        obj_user.new_tasks.pop(index-1)
    except ValueError:
        print("Not a valid number")
def delete_task(obj_user):
    view_tasks(obj_user)
    print()
    try:
        choice = int(input("For completed task choose: 1 , for new tasks choose: 2\n"))
        index = int(input("Enter Task Number: "))
        while True:
            if choice == 1:
                obj_user.completed_tasks.pop(index - 1)
                break
            elif choice == 2:
                print(obj_user.new_tasks.pop(index - 1))
                break
            else:
                choice = input("Please choose a valid number\n")
    except ValueError:
        print("Not a valid number")

def Quit(obj_user):

    try:
        with open(f"{obj_user.username}/new_task.pkl", "wb") as f:
            pickle.dump(obj_user.new_tasks, f)
            print("Task added successfully!")
    except Exception as e:
        print(f"Error adding task: {e}")

    try:
        with open(f"{obj_user.username}/completed_tasks.pkl", "wb") as f:
            pickle.dump(obj_user.completed_tasks, f)
            print("Task added successfully!")
    except Exception as e:
        print(f"Error adding task: {e}")

    return