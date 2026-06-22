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
            data['Tasks'].append({
                "Task name" : add,
                "Task status" : "Undone"
            })
        elif(opt == 2):
            print(data["Tasks"])
        elif(opt == 3):
            mark = input("Write the task name which you want to mark as done : ")
            for i in data['Tasks'] :
                if i['Tasks'] == mark :
                    data["Task status"] = "Done"
        elif(opt == 4):
            pass
        else : 
            print("Not a correct option.")

class notes:
    def call(self):
        print("Select from the following tasks to proceed :")
        print("1. Add Notes")
        print("2. View Notes")
        print("3. Exit")
        opt = int(input("Choose : "))
        if(opt == 1): 
            title = input("Write the note title : ")
            note = input("Write the note : ")
            data['Notes'].append({
                "Note title" : title,
                "Note" : note
                })
        elif(opt == 2):
            print(data["Notes"])
        elif(opt == 3): 
            pass
        else : 
            print("Not a correct option.")

task = tasks() 
note = notes()

while(True):
    print("WELCOME TO GRIZZ")
    print("Select from the following tasks to proceed :")
    print("1. Task Manager")
    print("2. Notes")
    print("3. Goals")
    print("4. Exit")
    
    opt = int(input("Choose :"))
    if(opt == 1):
        task.call()
    elif(opt == 2):
        note.call()
    elif(opt == 3):
        pass
    elif(opt == 4):
        break
