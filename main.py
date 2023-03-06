from admin import *
from user import *
a=Admin()
b=User()
print('**********************************Welcome to Restruant****************************************')
print('How may I help you?')
while True:
    print("*"*100)
    print('Press 1 to login as Admin')
    print('Press 2 to login as User')
    print('Press 3 to Exit')
    choice=int(input('Enter you choice :'))
    if choice==1:
        print("*"*100)
        print('Press 1 to add new flower')
        print('Press 2 to load flower')
        print('Press 3 to remove flower')
        print('Press 4 to edit flower')
        print("*"*100)
        option=int(input('Enter you option you want to perform :'))
        print("*"*100)
        if option==1:
            print(a.add_new_flower())
        elif option==2:
            print(a.load_flower())
        elif option==3:
            print(a.remove_flower())
        elif option==4:
            print(a.edit_flower())
        else:
            print('Please enter valid input')
    elif choice==2:
        print("*"*100)
        print('Press 1 for registeration')
        print('Press 2 for load registeration details')
        print('Press 3 for log in')
        print("*"*100)
        option=int(input('Enter you option you want to perform :'))
        print("*"*100)
        if option==1:
            print(b.registeration())
        elif option==2:
            print(b.load_registeration_details())
        elif option==3:
            b.log_in()
        else:
            print('Please enter valid input')
    elif choice==3:
        print('Thanks for visiting! Visit again')
        sys.exit()
    else:
        print('Please enter valid input')
        