def option_1():
    print("You have selected Option 1.")
    # Add code to perform action for option 1 here

def option_2():
    print("You have selected Option 2.")
    # Add code to perform action for option 2 here

def option_3():
    print("You have selected Option 3.")
    # Add code to perform action for option 3 here

def option_4():
    print("You have selected Option 4.")
    # Add code to perform action for option 4 here

def option_5():
    print("You have selected Option 5.")
    # Add code to perform action for option 5 here

def option_6():
    print("You have selected Option 6.")
    # Add code to perform action for option 6 here

def option_7():
    print("You have selected Option 7.")
    # Add code to perform action for option 7 here

def option_8():
    print("You have selected Option 8.")
    # Add code to perform action for option 8 here

def option_9():
    print("You have selected Option 9.")
    # Add code to perform action for option 9 here

def option_10():
    print("You have selected Option 10.")
    # Add code to perform action for option 10 here

def option_11():
    print("You have selected Option 11.")
    # Add code to perform action for option 11 here

def option_12():
    print("You have selected Option 12.")
    # Add code to perform action for option 12 here
    
options_functions = {
    1: option_1,
    2: option_2,
    3: option_3,
    4: option_4,
    5: option_5,
    6: option_6,
    7: option_7,
    8: option_8,
    9: option_9,
    10: option_10,
    11: option_11,
    12: option_12
}

options = {
    1: "creating a new mail",
    2: "using the same old mail",
    3: "retrieve the code from the mail",
    4: "open the mail page ",
    5: "getting a phone number default ",
    6: "chose an other phone number ",
    7: "try to retreive the code ",
    8: "chose an other one ",
    9: "create an image  ",
    10: "open the website to chose an image ",
    11: "create personal information ",
    12: "chose more than one function and get an output in a file or text"
 

}

print("Welcome to the options menu! Please choose an option:")
for i in options.keys():
    print(f"{i}.  {options[i]}")

choice = int(input("Enter your choice (1-12): "))

if choice in options_functions:
    options_functions[choice]()
else:
    print("Invalid choice! Please choose a number between 1 and 12.")