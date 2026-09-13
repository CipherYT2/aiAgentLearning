import sys

expenses = []

print("haha")

while True:
    print('wowoow')
    userInput = input("Input expense (type clear to clear)(amt|cat|note)(-1 to stop input)(d for expense editor): ")
    if userInput == '-1':
        break
    if userInput.lower() == 'd':
        break

    if userInput.lower() == "clear":
        confirmation = input("Confirm to clear all expenses (y/n)")
        try:
            if confirmation.lower() == 'y':
                with open("personalExpenseTrackerCommandLineTxtFile.txt", "w") as file:
                    pass
            elif confirmation.lower() == 'n':
                pass
        except Exception as e:
            pass
    else:
        with open("personalExpenseTrackerCommandLineTxtFile.txt", "a") as file:
            file.write(userInput + "\n")
            
def readFile():
    with open("personalExpenseTrackerCommandLineTxtFile.txt", "a") as file:
        pass
    with open("personalExpenseTrackerCommandLineTxtFile.txt", "r") as file:
        lines = file.readlines()
    return lines

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

def deleteExpense():
    lines = readFile()
    for line in lines:
        print(line)
    delete = input("Input price|cat|note to delete: ")
    try:
        for line in lines:
            if line == delete:
                with open("personalExpenseTrackerCommandLineTxtFile.txt", "w") as file:
                    for line in lines:
                        if line != delete:
                            file.write(line)
    except Exception as e:
        print("Line does not exist! ")


displaySpecificExpenses()
displayExpenses()
