import os
import time

BUDGET_FILE = "budget.txt"
BASE_BUDGET_FILE = "baseBudget.txt"
EXPENSE_FILE = "expenses.txt"
CATEGORY_FILE = "categories.txt"
DATE_FILE = "dates.txt"

def main():
    budget = 0
    budget = load_budget(budget)
    base_budget = load_base_budget()
    expenses = []
    load_expense(expenses)
    categories = []
    load_category(categories)
    dates = []
    load_date(dates)

    print("-------------WELCOME TO BUDGET TRACKER-----------------")
    while True:
        option = show_option_menu()
        if option == 1:
            budget = add_to_budget(budget)
            base_budget = budget
            save_base_budget(base_budget)
        elif option == 2:
            budget = add_expense(budget,expenses,categories,dates)
            check_warning(budget,base_budget)
        elif option == 3:
            show_expenses(expenses,categories,dates)
        elif option == 4:
            search_expense_by_category(expenses,categories,dates)
        elif option == 5:
            search_expense_by_date(expenses,categories,dates)
        elif option == 6:
            show_current_budget(budget)
        elif option == 7:
            reset_budget_traker(expenses,categories,dates)
            budget = 0
            base_budget = 0
        else:
            print("\n\n-------THANKS FOR USING OUR APP!--------")
            print("------------SEE YOU LATER----------------")
            exit()

    

def show_option_menu():
    #shows the options: Add to budget, Add expense,Show expenses, search expense by category, search expense by date, show current budget
    print("\n\n---------Menu----------")
    print("1. Add to budget")
    print("2. Add expense")
    print("3. Show expenses")
    print("4. Search expense by category")
    print("5. Search expense by date")
    print("6. Current budget")
    print("7. Reset budget tracker")
    print("8. Exit")

    #selecting option by user promt
    option = input("Select an option: ")
    if option.isdigit():
        option = int(option)
        if option > 0 and option <= 8:
            return option
        else:
            print("\n\nPLEASE SELECT A VALID OPTION!")
            return show_option_menu()
    else:
        print("\n\nPLEASE SELECT A VALID OPTION!")
        return show_option_menu()
    

def add_to_budget(budget):
    #gets user input budget and updates budget
    money = input("\n\nEnter the budget to add: ")
    while not money.isdigit():
        money = input("\n\nPLEASE ENTER VALID BUDGET AMOUNT: ")
    money = float(money)
    budget += money
    show_current_budget(budget)
    save_budget(budget)
    return budget



def add_expense(budget,expenses,categories,dates):
    #gets expense with category and date
    money = input("\n\nEnter the expense: ")
    while not money.isdigit():
        money = input("\n\nPLEASE ENTER VALID EXPENSE AMOUNT: ")
    money = float(money)
    while money > budget:
        money = input("\n\nYOUR EXPENSE GOES BEYOND YOUR BUDGET! PLEASE ENTER VALID EXPENSE AMOUNT: ")
    expenses.append(money)
    catagory = input("Enter the category of the expense: ")
    categories.append(catagory)
    date = input("Enter the date of the expense(DD/MM/YY): ")
    dates.append(date)
    budget -= money
    show_current_budget(budget)
    save_budget(budget)
    save_expense(expenses)
    save_category(categories)
    save_date(dates)
    return budget



def check_warning(budget,base_budget):
    #warns if the current budget in lest than 10% of the budget added 
    if budget <= (base_budget*0.1):
        print("WARNING! YOU HAVE LESS OR EQUAL 10% OF BUDGET LEFT!")




def show_expenses(expenses,categories,dates):
    #shows the full expense list
    total = 0
    length = len(expenses)
    if length == 0:
        print("NO EXPENSE RECORD!")
    else:
        print("------YOUR EXPENSES--------")
        print("Amount\t - \tDate\t - \tCategory")
        print("-----------------------------------------------------------------")
        for i in range(length):
            print(expenses[i],"\t - \t",dates[i],"\t - \t",categories[i])
            total += expenses[i]
        
        print("-----------------------------------------------------------------")
        print("Total =",total)



def search_expense_by_category(expenses,categories,dates):
    #searches expense by user given category
    total = 0
    user_category = input("Enter the category to see expenses of: ")
    if user_category not in categories:
        print("THIS CATEGORY HAS NO RECODED EXPENSE!")
    else:
        length = len(expenses)
        print("------YOUR EXPENSES OF CATEGORY",user_category,"--------")
        print("Amount\t - \tCategory")
        print("-----------------------------------------------------------------")
        for i in range(length):
            if categories[i] == user_category:
                print(expenses[i],"\t - \t",dates[i])
                total += expenses[i]
    print("-----------------------------------------------------------------")
    print("Total =",total)


def search_expense_by_date(expenses,categories,dates):
    #searches expense by user given date
    total = 0
    user_date = input("Enter the date to see expenses from: ")
    if user_date not in dates:
        print("THIS DATE HAS NO RECODED EXPENSE!")
    else:
        length = len(expenses)
        print("------YOUR EXPENSES IN",user_date,"--------")
        print("Amount\t - \tCategory")
        print("-----------------------------------------------------------------")
        for i in range(length):
            if dates[i] == user_date:
                print(expenses[i],"\t - \t",categories[i])
                total += expenses[i]
    print("-----------------------------------------------------------------")
    print("Total =",total)



def show_current_budget(budget):
    #shows current budget
    print("\n\nYour current budget is",budget)


def save_budget(budget):
    #saves added budget to text file
    global BUDGET_FILE
    f = open(BUDGET_FILE,'w+')
    f.writelines(str(budget))


def save_base_budget(base_budget):
    #saves base budget to text file
    global BASE_BUDGET_FILE
    f = open(BASE_BUDGET_FILE,'w+')
    f.writelines(str(base_budget))


def save_expense(expenses):
    #save expenses to text file
    global EXPENSE_FILE
    f = open(EXPENSE_FILE,"w+")
    for expense in expenses:
        expense = str(expense)
        f.writelines(f"{expense}\n")


def save_category(categories):
    #save categories for the expenses to text file
    global CATEGORY_FILE
    f = open(CATEGORY_FILE,"w+")
    for category in categories:
        f.writelines(f"{category}\n")



def save_date(dates):
    #saves dates of expenses to text file
    global DATE_FILE
    f = open(DATE_FILE,"w+")
    for date in dates:
        f.writelines(f"{date}\n")

def load_budget(budget):
    #loads budget saved in text file when the code is run
    global BUDGET_FILE
    if os.path.exists(BUDGET_FILE) and os.path.getsize(BUDGET_FILE) != 0:
        f = open(BUDGET_FILE,"r+")
        budget = float(f.read())
        return budget
    else:
        return 0
    

def load_base_budget():
    #loads base budget saved in text file when the code is run
    global BASE_BUDGET_FILE
    if os.path.exists(BASE_BUDGET_FILE) and os.path.getsize(BASE_BUDGET_FILE) != 0:
        f = open(BASE_BUDGET_FILE,"r+")
        base_budget = float(f.read())
        return base_budget
    else:
        return 0

def load_expense(expenses):
    #loads expenses saved in text file when the code is run
    global EXPENSE_FILE
    if os.path.exists(EXPENSE_FILE) and os.path.getsize(EXPENSE_FILE) != 0:
        f = open(EXPENSE_FILE,"r+")
        for line in f:
            line = line.strip()
            expenses.append(float(line))
    else:
        pass


def load_category(categories):
    #loads categories saved in text file when the code is run
    global CATEGORY_FILE
    if os.path.exists(CATEGORY_FILE) and os.path.getsize(CATEGORY_FILE) != 0:
        f = open(CATEGORY_FILE,"r+")
        for line in f:
            line = line.strip()
            categories.append(line)
    else:
        pass


def load_date(dates):
    #loads dates saved in text file when the code is run
    global DATE_FILE
    if os.path.exists(DATE_FILE) and os.path.getsize(DATE_FILE) != 0:
        f = open(DATE_FILE,"r+")
        for line in f:
            line = line.strip()
            dates.append(line)
    else:
        pass


def reset_budget_traker(expenses,categories,dates):
    #removes all the data
    print("\nCleaning all the data......")
    
    global BUDGET_FILE,BASE_BUDGET_FILE,EXPENSE_FILE,CATEGORY_FILE,DATE_FILE
    if os.path.exists(BUDGET_FILE):
        open(BUDGET_FILE,"w").close()
    if os.path.exists(BASE_BUDGET_FILE):
        open(BASE_BUDGET_FILE,"w").close()
    if os.path.exists(EXPENSE_FILE):
        open(EXPENSE_FILE,"w").close()
    if os.path.exists(CATEGORY_FILE):
        open(CATEGORY_FILE,"w").close()
    if os.path.exists(DATE_FILE):
        open(DATE_FILE,"w").close()

    expenses.clear()
    categories.clear()
    dates.clear()

    time.sleep(1)
    print("Budget Traker reset completed!")




if __name__ == '__main__':
    main()