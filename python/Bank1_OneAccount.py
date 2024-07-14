# Non-OOP
#Bank Version 1
#Single Account

accountName = 'Joe'
accountBalance = 100
accountPassword = 'Soup'

while True:
    print()
    print('Press b to get balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawl')
    print('Press s to show the account')
    print('Press q to quit')
    print()
    
    action = input('What do you want to do? ')
    action = action.lower() #force the lowercase
    action = action[0] #Just use the first letter
    
    if action == 'b':
        print('Get Balance')
        userPassword = input('What is your password ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            print('Your account balance is ', accountBalance)
            
    elif action == 'd':
        print('Deposit: ')
        userDepositAmount = input("How much would you like to depsoit today? ")
        userDepositAmount = int(userDepositAmount)
        userPassword = input("Enter your password: ")
        
        if userDepositAmount < 0:
            print('You cannot deposit a negative amount')
            
        elif userPassword != accountPassword:
            print('Incorrect password ')
            
        else:
            accountBalance = accountBalance + userDepositAmount
            print('Your new balance is: ', accountBalance)
            
            
    elif action == 's': #show
        print('Show: ')
        print('   Name', accountName)
        print('   Name', accountBalance)
        print('   Name', accountPassword)
        print()
        
    elif action =='q':
        break
    
    elif action  == 'w':
        print('Withdraw: ')
        
        userWithdrawAmount = input('Please enrter the amount yo withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter your password: ')
        
        if userWithdrawAmount < 0:
            print('You cannot enter a negative amount. ')
            
        elif userPassword != accountPassword:
            print('Incorrect password')
            
        elif userWithdrawAmount > accountBalance:
            print('You do not have the funds for this withdrawl')
            
        else: #ok
            accountBalance = accountBalance - userWithdrawAmount
            print('Your new account balance is: ', accountBalance)
            
    print('Done')