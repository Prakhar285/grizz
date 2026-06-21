print("WELCOME TO GRIZZ")
print("Select from the following tasks to proceed :")
print("1. Task Manager")
print("2. Notes")
print("3. Goals")
print("4. Exit")

class tasks():
    def call():
        print("Select from the following tasks to proceed :")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Tasks Complete")
        print("4. Exit")
        opt = input("Choose tasls: ")
        if(opt == 1): 
            print("option 1 selected ")

o = int(input("Choose : "))
if o == 1 : 
    tasks.call()