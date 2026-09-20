import sys


tasks = {}

def readFile():
    with open("todoListStorage.txt", "a") as file:
        pass
    with open("todoListStorage.txt", "r") as file:
        lines = file.readlines()
    return lines

for line in readFile():
    tasks[line.split(', ')[0]] = line.split(', ')[1]

try:
    while(True):
        mode = input("\n1. Add Task \n2. Remove Task \n3. View Tasks \n4. Mark Task as Done \n5. Exit \nInput: ")

        if mode == '1':
            tasks[input("Task: ")] = False
            with open("todoListStorage.txt", "a") as file:
                for key in tasks:
                    file.write(key + f", {tasks[key]} \n")
            
        if mode == '2':
            lines = readFile()
            for line in lines:
                print(line)

            delete = input("Input Line you Want to Delete: ")
            try:
                for line in lines:
                    if line.rstrip() == delete.rstrip():
                        with open("todoListStorage.txt", "w") as file:
                            for line in lines:
                                if line.rstrip() != delete:
                                    file.write(line)
            except Exception as e:
                print("Line does not exist. ")

        if mode == '3':
            taskCt = 1
            for line in readFile():
                print(str(taskCt) + f". {line}")
                taskCt += 1

        if mode == '4':
            lineCt = 0
            for line in readFile():
                taskKey = line.strip().split(', ')[0]

                if taskKey in tasks:
                     print(f"{taskKey}, {tasks[taskKey]}")
                else:
                    print(f"Task Key was not found. Task Key: {taskKey}")


                editDone = input("Mark Task as Done? (y/n): ")
                if editDone.lower() == 'y':
                    tasks[(line.split(', ')[0])] = True
                else:
                    tasks[(line.split(', ')[0])] = False
                lineCt += 1


            with open("todoListStorage.txt", "w"):
                pass
            with open("todoListStorage.txt", "a") as file:
                for key in tasks:
                    file.write(key + f", {tasks[key]} \n")


        if mode == '5':
            break


except KeyboardInterrupt:
    sys.exit(0)
                            
