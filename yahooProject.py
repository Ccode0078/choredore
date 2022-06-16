#answer = input('y or n?')
#answer = ""
userInput = ""
print("welcome to www.yahoo.com")
while True:
    print('Enter login information')
    print('Press i to view inbox ')
    print('Click x to logoff')
    userInput = input('user: Please choose any command')
    if userInput == "Code_corbin289":
        userInput = input('please enter password')
        print('welcome back user!')
        password = input('Daily news:  inflation at all time high| Nasdaq falls 100 points|FOMC meeting at 2:30pm')
        userInput = input('press r to return to home')
        break
        
     

    elif userInput == "x":
        break
        
    elif userInput == 'i':
        messages = 300
        junk = 30 
        spam = 20 
        print('you have {0}  unreadMessages| {1} junkMail | {2} spam '.format(messages, junk, spam))
        print('www.Fedex.com/tracking order: your package has been sent. would you like to track your order?')
        userInput = input('y or n?')
    if  userInput == 'y': 
        print('your tracking number #5689789 has been sent ')     
        print('3s ago.') 
    elif userInput == 'n':
        print('okay, going back to home->>')
      
        userInput = input('press r to return to home screen')
    elif userInput == 'r':
        break
    else:
        print('please enter valid input')

       


       





    
        
        
        
        
       
       

       
        
