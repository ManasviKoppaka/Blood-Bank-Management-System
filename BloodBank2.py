def hr():
    print("-----------------------------------------------")
def hr2():
    print("_______________________________________________")
def hr3():
    print("***********************************************")

print("|======================================================|")
print("|           *********************************          |")
print("|              Blood Bank Management System            |")
print("|                   By Manasvi Koppaka                 |")
print("|           *********************************          |")
print("|======================================================|")

def signup():
    hr2()
    print("Welcome! Enter the following details to set up your account")
    hr()
    username = input("Enter the username: ")
    if username == "":
        print("Invalid username. Try Again")
        return
    db = open("File.txt", "r")
    for data in db:
        u,p = data.split(",")
        if username == u:
            print("Username has already been used. Try Again")
            return
    db.close()

    
    password = input("Enter the password. It must contain minimum 5 characters, a capital letter, a special character (@, #, *, !) and a number")
    special = ["@", "#", "*", "!"]
    if len(password) < 5:
        print("The password must contain atleast 5 characters. Try Again")
        signup()
    cap = False
    for i in password:
        if i.isupper():
            cap = True
            break
    if cap == False:
        print("The password must contain atleast 1 capitalized character. Try Again")
        return 

    sp = False
    for i in special:
        if i in password:
            sp = True
            break
    if sp == False:
        print("The password must contain atleast 1 special character. Try Again")
        return 

    num = False
    for i in password:
        if i.isnumeric():
            num = True 
            break
    if num == False:
        print("The password must contain atleast 1 number. Try Again")
        return

    confirm_password = input("Enter your password again: ")
    if password != confirm_password:
        print("The password and confirm password are not matching. Try Again ")
        return


    data = username + "," + password
    db = open("File.txt", "a")
    db.write(data)
    db.write("\n")
    db.close()
    hr2()
    print("Your account has been created succesfully!")
    hr2()
    return


def login():
    print("Welcome Back! Please enter the following details to log in succesfully")
    username = input("Enter your username: ")
    db = open("File.txt", "r")
    flag = 0
    for i in db:
        u,p = i.split(",")
        if username == u:
            flag = 1
            break
    db.close()
    if flag == 0:
        print("Username doesn't exist. Try Again")
        return
    password = input("Enter your password: ")
    hr()
    password = password+"\n"
    if password != p:
        print("Incorrect Password. Try Again")
        return
    hr2()
    print("Login Succesfull!")
    hr2()
    print("|======================================================|")
    print("|           *********************************          |")
    print("|              Blood Bank Management System            |")
    print("|                   By Manasvi Koppaka                 |")
    print("|           *********************************          |")
    
    #Initializing quantity
    quantity = {
        "A+" : 0,
    "O+" : 0,
    "B+" : 0,
    "AB+" : 0,
    "A-" : 0,
    "O-" : 0,
    "B-" : 0,
    "AB-" : 0
    }
    
    #Fetching the quantity from the data base
    db = open("dataBase.txt", "r")
    for i in db:
        bg,qty = i.split(",")
        for j in quantity.keys():
            if bg == j:
                quantity[j] = int(qty)
    db.close()
    
    #Blood Seeking Rules
    bsr = {
    "A+" : ["A+", "A-", "O+", "O-"],
    "O+" : ["O+", "O-"],
    "B+" : ["B+", "B-", "O+", "O-"],
    "AB+" : ["A+", "B+", "O+", "AB+", "A-", "B-", "O-", "AB-"],
    "A-" : ["A-", "O-"],
    "O-" : ["O-"],
    "B-" : ["B-", "O-"],
    "AB-" : ["A-", "B-", "O-", "AB-"] 
    }
    
    #Updating the Data Base every time when someone donates or takes blood
    def updateDataBase():
        db = open("dataBase.txt", "w")
        for i in quantity.keys():
            record = f"{i},{quantity[i]}"+"\n"
            db.write(record)
    
    #Updating the Rewards every time someone donates blood
    def updateReward(name,type,qty):
        record = f"{name} -> {type} -> {qty}"+"\n"
        db = open("rewards.txt", "a")
        db.write(record)
        db.close()
    
    #Showing the people who donated the blood
    def showRewards():
        db = open("rewards.txt", "r")
        for i in db:
            print(i)
        db.close()   
    
    #Blood Seeking code
    def bloodSeeker():
        type = input("Enter your blood type: ")
        if type != "A+" and type != "A-" and type != "B+" and type != "B-" and type != "O+" and type != "O-" and type != "AB+" and type != "AB-":
          print("Invalid Input. Try Again.")
          return
        for i in bsr.keys():
            if i == type:
                print("Blood Groups for the patient: ")
                for j in bsr[i]:
                    print(j, quantity[j], "ml")
    
        bloodChoice = input("Select the blood group: ")
        if bloodChoice != "A+" and bloodChoice != "A-" and bloodChoice != "B+" and bloodChoice != "B-" and bloodChoice != "O+" and bloodChoice != "O-" and bloodChoice != "AB+" and bloodChoice != "AB-":
          print("Invalid Input. Try Again.")
          return
        bloodQuantity = input("Enter quantity in ml: ")
        num = False
        if bloodQuantity.isnumeric():
          num = True
          bloodQuantity1 = int(bloodQuantity)
        if num == False:
          print("Invalid Input")
          return
        for i in quantity.keys():
            if i == bloodChoice:
                if bloodQuantity1 < quantity[i]:
                    quantity[i] -= bloodQuantity1
                    updateDataBase()
                else:
                    print("Blood not suffiecient.")
    
    
    #Blood Donating Code
    def donateBlood():
        name = input("Enter the name of the donor: ")
        type = input("Enter your Blood Type: ")
        if type != "A+" and type != "A-" and type != "B+" and type != "B-" and type != "O+" and type != "O-" and type != "AB+" and type != "AB-":
          print("Invalid Input. Try Again.")
          return
        qty = input("Enter the quantity: ")
        num = False
        if qty.isnumeric():
          num = True
          qty1 = int(qty)
        if num == False:
          print("Invalid Input")
          return
        for i in quantity.keys():
            if i == type:
                quantity[i]+=qty1
                updateDataBase()
                updateReward(name,type,qty1)
    
    def showDataBase():
        db = open("dataBase.txt", "r")
        print("BG,qty")
        for i in db:
            print(i, end = "")
        db.close()
    
        #Alerts!
        print("Alert Messages - ")
        print("***************************************************")
        for i in quantity.keys():
            if quantity[i] <= 200:
                print(f"ALERT! {i} is available in less quantity. Donation required")
        print("***************************************************")
    options  = ["Blood Seeker", "Blood Donation", "Rewards and Recognitions", "Show Current Statistics", "Exit"]
    
    
    #Main Code
    while True:
        print("========================================================")
        for i in range(len(options)):
            print(i+1, "-", options[i])
        print("--------------------------------------------------------")
        choice = input("Enter your choice: ")
        if choice == "1":
            bloodSeeker()
        elif choice == "2":
            donateBlood()
        elif choice == "3":
            showRewards()
        elif choice == "4":
            showDataBase()
        elif choice == "5":
            print("Thank You")
            break
        else:
            print("Invalid Input. Try Again")
#Main Program
while True:
    hr3()
    print("1 - Signup")
    print("2 - Login")
    print("3- Exit")
    hr3()
    option = int(input("Enter your option: "))
    if option == 1:
        signup()
    elif option == 2:
        login()
    elif option == 3:
        break
    else:
        print("Invalid Input")