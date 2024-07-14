#Non-OOP
#Bank 2
#Single Account

accountName = ''
accountBalance = 0 
accountPassword = ''

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password
    
def show():
    global accountName, accountBalance, accountPassword
    print('     Name', accountName)
    print('     Balance', accountBalance)
    print('     Password', accountPassword)
    print()
    
    

def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print("Incorrect password")
        return None
    return accountBalance

def deposit(amountDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountDeposit < 0: 
        print('You cannot enter a negative number ')
        return None
    if password != accountPassword:
        print("You have entered an incorrect password ")
        return None
    accountBalance = accountBalance + amountDeposit
    return accountBalance

def withdraw(amountwitdraw, password):
    global accountName, accountBalance, accountPassword
    if amountwitdraw < 0:
        print('You cannot withdraw a negative amount ')
        return None
        
    if password != accountName:
        print('Incorrect Password')
        return None
    
    if amountwitdraw > accountBalance:
        print('You do not have the funds to make this withdrawl')
        return None
    accountBalance = accountBalance - amountwitdraw
    return accountBalance

newAccount ('Joe' , 100, 'Soup') #Craete an account

while True:
    print()
    print('Press b to get the balance ')
    print('Press d to make a deposit ')
    print('Press w to make a withdrawl ')
    print('Press s to show the account ')
    print()
    
    
    action = input("What would you like to do? ")
    action = action.lower
    action = action[0]
    print()
    
    if action == 'b':
        print('Get Balance ')
        userPassword = input("Please enter a password ")
        theBalance = theBalance(userPassword)
        if theBalance is not None:
            print('You balance is ', theBalance)
            
    elif action == 'd':
        print("Deposit: ")
        userDepositAmount = input("Please enter the amount to deposit: ")
        
    
        
    
    