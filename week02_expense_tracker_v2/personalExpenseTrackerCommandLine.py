import sys

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
