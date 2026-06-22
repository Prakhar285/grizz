import pathlib

print("WELCOME TO GRIZZ")
print("Select from the following tasks to proceed :")
print("1. Task Manager")
print("2. Notes")
print("3. Goals")
print("4. Exit")

data = {"Tasks" : [],"Notes" : [],"Goals" : []}
database = "grizzbase.json"

class tasks:
    def call(self):
        print("Select from the following tasks to proceed :")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Tasks Complete")
        print("4. Exit")
        opt = int(input("Choose : "))
        if(opt == 1): 
            add = input("Write the task name which you want to add : ")
        elif(opt == 2):
            pass
        elif(opt == 3):
            mark = input("Write the task name which you want to mark as done : ")
        elif(opt == 4):
            pass
        else : 
            print("Not a correct option.")

class notes:
    print("Select from the following tasks to proceed :")
    print("1. Add Notes")
    print("2. View Notes")
    opt = int(input("Choose : "))
    if(opt == 1): 
        title = input("Write the note title : ")
        note = input("Write the note : ")
    elif(opt == 2):
        pass