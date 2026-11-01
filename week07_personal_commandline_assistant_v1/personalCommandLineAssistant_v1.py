import sys



def expenseTracker():
    expenses = []

    deleteMode = False

    def readFile():
        with open("personalExpenseTrackerCommandLineTxtFile.txt", "a") as file:
            pass
        with open("personalExpenseTrackerCommandLineTxtFile.txt", "r") as file:
            lines = file.readlines()
        return lines

    def deleteExpense():
        lines = readFile()
        for line in lines:
            print(line)
        delete = input("Input price|cat|note to delete: ")
        try:
            for line in lines:
                if line.rstrip() == delete:
                    with open("personalExpenseTrackerCommandLineTxtFile.txt", "w") as file:
                        for line in lines:
                            if line.rstrip() != delete:
                                file.write(line)
        except Exception as e:
            print("Line does not exist! ")

    def displayMonthSummary():
        lines = readFile()
        monthExpense = {
            "01": 0,
            "02": 0,
            "03": 0,
            "04": 0,
            "05": 0,
            "06": 0,
            "07": 0,
            "08": 0,
            "09": 0,
            "10": 0,
            "11": 0,
            "12": 0
        }
        for line in lines:
            try:
                monthExpense[f"{((line.split('|')[3]).split('/'))[1].rstrip()}"] = monthExpense[f"{((line.split('|')[3]).split('/'))[1].rstrip()}"] + int((line.split('|'))[0].rstrip())
            except IndexError:
                print("IndexError")

        print(f"January: {monthExpense["01"]}")
        print(f"February: {monthExpense["02"]}")
        print(f"March: {monthExpense["03"]}")
        print(f"April: {monthExpense["04"]}")
        print(f"May: {monthExpense["05"]}")
        print(f"June: {monthExpense["06"]}")
        print(f"July: {monthExpense["07"]}")
        print(f"August: {monthExpense["08"]}")
        print(f"September: {monthExpense["09"]}")
        print(f"October: {monthExpense["10"]}")
        print(f"November: {monthExpense["11"]}")
        print(f"December: {monthExpense["12"]}")


    while True:
        userInput = input(f"1. Input Expense(s) \n 2. Delete Expense \n 3. View Summary \n 4. Clear Expenses \n 5. Exit \n Input: ")

        if userInput == '1':
            inputedExpense = input("Input expense (amt|cat|note|date): ")
            with open("personalExpenseTrackerCommandLineTxtFile.txt", "a") as file:
                file.write(inputedExpense + f"\n")

        if userInput == '5':
            break

        if userInput.lower() == '2':
            deleteMode = True
            deleteExpense()
            deleteMode = False

        if userInput == '3':
            displayMonthSummary()        

        if userInput.lower() == "4":
            confirmation = input("Confirm to clear all expenses (y/n)")
            try:
                if confirmation.lower() == 'y':
                    with open("personalExpenseTrackerCommandLineTxtFile.txt", "w") as file:
                        pass
                elif confirmation.lower() == 'n':
                    pass
            except Exception as e:
                pass
                    
    def displayExpenses():
        lines = readFile()
        for line in lines:
            try:
                parts = line.strip().split('|')
                amount = parts[0].strip()
                category = parts[1].strip()
                note = parts[2].strip()
                expenses.append(f"{amount} | {category} | {note}")
                if not expenses:
                    print("No expenses recorded yet!")
                else:
                    print("----------------------")
                    print("Expenses:")
                    for line in expenses:
                        print(line)
                    print("----------------------")
            except IndexError:
                print("IndexError")

    def displaySpecificExpenses():
        lines = readFile()
        totalAmt = 0
        categoryTotals = {}
        for line in lines:
            try:
                parts = line.strip().split('|')
                amount = float(parts[0])
                category = parts[1]
                totalAmt += amount
                if category in categoryTotals:
                    categoryTotals[category] += amount
                else:
                    categoryTotals[category] = amount
            except IndexError:
                print("IndexError")
        print(f"Total Amount: {totalAmt}")
        print("Category Totals:")
        for category, total in categoryTotals.items():
            print(f"{category}: {total}")

    if deleteMode == False:
        displaySpecificExpenses()
        displayExpenses()
        displayMonthSummary()
    deleteMode = False


def todoList():
    tasks = {}

    def readFile():
        with open("/Users/OL/agentProjects/aiAgentLearning/week07_personal_commandline_assistant_v1/todoListStorage.txt", "a") as file:
            pass
        with open("/Users/OL/agentProjects/aiAgentLearning/week07_personal_commandline_assistant_v1/todoListStorage.txt" , "r") as file:
            lines = file.readlines()
        return lines

    for line in readFile():
        print(line)
        tasks[line.split(', ')[0]] = line.split(', ')[1]

    try:
        while(True):
            mode = input("\n1. Add Task \n2. Remove Task \n3. View Tasks \n4. Mark Task as Done \n5. Exit \nInput: ")

            if mode == '1':
                tasks[input("Task: ")] = False
                with open("/Users/OL/agentProjects/aiAgentLearning/week07_personal_commandline_assistant_v1/todoListStorage.txt", "w") as file:
                    for key in tasks:
                        file.write(key + f", {tasks[key]}")
        
            if mode == '2':
                lines = readFile()
                for line in lines:
                    print(line)

                delete = input("Input Line you Want to Delete: ")
                try:
                    for line in lines:
                        if line.rstrip() == delete.rstrip():
                            with open("/Users/OL/agentProjects/aiAgentLearning/week07_personal_commandline_assistant_v1/todoListStorage.txt", "w") as file:
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
                    
def password():
    import ollama

    def checkPasswordStrength(password):
        stream = ollama.chat(
            model='gemma2',
            messages=[{
                'role': 'user',
                'content': f'Check the strength of the password provided at the end of the line. Make sure your output is only Password strength followed bylow, moderate, or high, high being the highest security. Inputted password: {password}'
            }],
            stream=True
        )
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)

    def generatePassword(length, easyRememberance):
        full_response = ""
        stream = ollama.chat(
            model='gemma2',
            messages=[{
                'role': 'user',
                'content': f'Generate a password where the length is {length} and how easy it is to remember to a human brain is {easyRememberance}, 10 is the easiest to remember and 0 is the absolute securest you can make. Do NOT generate any additional text. After that generate the strength of the password. Make the strength formated like in a new line and like: Generated password strength: low, medium or high. The format in which you should print is: Generated password: [password]'
            }],
            stream=True
        )
        for chunk in stream:
             content = chunk.message.content
             print(content, end='', flush=True)
             full_response += content
        return full_response.replace("Generated password: ", "")
    while True:
        mode = input("1. Check password strength \n2. Generate password \n3. Exit \nInput: ")

        if mode == '3':
            break
    
        if mode == '2':
            print("PASSWORD GENERATOR \n")
            try:
                length, remember = input("Input the length, and how easy you want the password to be(10 is the easiest, 0 most secure). Format is (length, rememberance): ").split(', ')
                generatePassword(length, remember)
            except Exception as e:
                print("Unsupported Format.")

        if mode == '1':
            print("PASSWORD STRENGTH CHECKER \n")
            password = input("Input your password: ")
            checkPasswordStrength(password)

def weather():
    import requests
    import ollama
    from geopy.geocoders import Nominatim

    geolocator = Nominatim(user_agent="city_coordinates_app")

    city = input("Input your city: ")
    location = geolocator.geocode(city)
    if location:
        lat = location.latitude
        lon = location.longitude
    else:
        print("Location not found.")
    api_key = "4f49f3dfb73a0708d266491fb70ea86c"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    temp = data["main"]["temp"]
    weather = f"{data["weather"][0]["main"]}, {data["weather"][0]["description"]}"

    print(f"\ntemp: {temp} \nweather: {weather}")

    def giveWeatherAdvice(weather):
        stream = ollama.chat(
            model='gemma2',
            messages=[{
                'role': 'user',
                'content': f'Based on the weather provided that is in a dictionary form, give advice in a fun way however keep it short no more than 10 words but keep it fun and kind with emojis e.g. if it is raining: Take an umbrella ☔. Here is the data: {data}'
            }],
            stream=True
        )
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)

    giveWeatherAdvice(data)

while True:
    mode = input("====Personal Assistant V1====\n1. Expense Tracker \n2. To-do List \n3. Password Manager \n4. Weather \n5. Quit \nInput: ")

    if mode == '1':
        expenseTracker()
    elif mode == '2':
        todoList()
    elif mode == '3':
        password()
    elif mode == '4':
        weather()
    else:
       break
