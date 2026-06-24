from pathlib import Path
import json

data = {"Tasks" : [],"Notes" : [],"Goals" : []}
database = "grizz_base.json"

if Path(database).exists():
    with open(database,'r') as f :
        content = f.read()
        if (content):
            data = json.loads(content)

def save():
    with open(database,'w') as f :
        json.dump(data,f,indent=4)

def get_choice():
    while(True):
        try:
            opt = int(input("Choose : "))
            return opt
        except(ValueError):
            print("Put some integer man.")

class TaskManager:
    def call(self):
        print("Select from the following tasks to proceed :")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Tasks Complete")
        print("4. Exit")
        opt = get_choice()
        if(opt == 1): 
            add = input("Write the task name which you want to add : ").strip()
            if not add:
                print("Cant be empty!!")
                return
            for i in data['Tasks']:
                if i['Task name'].lower() == add.lower() :
                    print("Task name already exists.")
                    return
            data['Tasks'].append({
                "Task name" : add,
                "Task status" : "Undone"
            })
            save()
            print("Task saved.")
        elif(opt == 2):
            x = 1
            if not data['Tasks']:
                print("No tasks available.")
                return
            for i in data['Tasks']:
                print(f"Task {x}.")
                print()
                print(f"Task : {i['Task name']}")
                print(f"Status : {i['Task status']}")
                print()
                x += 1
        elif(opt == 3):
            mark = input("Write the task name which you want to mark as done : ")
            search = False
            for i in data['Tasks'] :
                if i['Task name'].lower() == mark.lower() :
                    i["Task status"] = "Done"
                    search = True
                    save()
                    print("Task status modified")
                    break
            if not search:
                print("Task not found.")
        elif(opt == 4):
            pass
        else : 
            print("Not a correct option.")

class NotesManager:
    def call(self):
        print("Select from the following tasks to proceed :")
        print("1. Add Notes")
        print("2. View Notes")
        print("3. Exit")
        opt = get_choice()
 
        if(opt == 1): 
            title = input("Write the note title : ").strip()
            note = input("Write the note : ").strip()
            if not title and not note :
                print("Write Something!!")
            data['Notes'].append({
                "Note title" : title,
                "Note" : note
                })
            save()
            print("Your note is saved.")
        elif(opt == 2):
            x = 1
            if not data["Notes"]:
                print("No notes available.")
                return
            for i in data["Notes"]:
                print(f"Note {x}.")
                print()
                print(f"Note Title : {i['Note title']}")
                print(f"Note : {i['Note']}")
                print()
                x += 1
            
        elif(opt == 3): 
            pass
        else : 
            print("Not a correct option.")

task = TaskManager() 
note = NotesManager()

while(True):
    print()
    print("WELCOME TO GRIZZ")
    print("Select from the following tasks to proceed :")
    print("1. Task Manager")
    print("2. Notes")
    print("3. Goals")
    print("4. Exit")
    opt = get_choice()

    if(opt == 1):
        task.call()
    elif(opt == 2):
        note.call()
    elif(opt == 3):
        pass
    elif(opt == 4):
        break
    else: 
        print("Not a correct Option.")