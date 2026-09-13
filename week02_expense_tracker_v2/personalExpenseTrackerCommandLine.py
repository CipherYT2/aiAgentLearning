import sys

expenses = []

print("haha")

while True:
    print('wowoow')
    userInput = input("Input expense (type clear to clear)(amt|cat|note)(-1 to stop input): ")
    if userInput == '-1':
        break

    if userInput.lower() == "clear":
        with open("personalExpenseTrackerCommandLineTxtFile.txt", "w") as file:
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


displaySpecificExpenses()
displayExpenses()
