import random
import json
import sys
class User:
    def __init__(self):
        self.register={}
        self.order_history={}
        self.place_order_list=[]
    def registeration(self):
        self.name=input('Enter your name :')
        self.ph_no=int(input('Enter your phone number :'))
        self.address=input('Enter your address :')
        self.email=input('Enter your email :')
        self.password=input('Enter your password :')
        self.registeration_details={'Name':self.name,'Phone_no':self.ph_no,'Address':self.address,'Email':self.email,'Password':self.password}
        if self.email not in self.register:
            self.register[self.email]=self.registeration_details
            with open('registeration.json','w') as f:
                json.dump(self.register,f,indent=4)
            print('Registeration successful') 
        else:
            print('You are already registered')
        return ''
    def load_registeration_details(self):
        with open('registeration.json','r') as f:
            self.register=json.load(f)
        return self.register
    
    def log_in(self):
        email_id=input('Enter the email address :')
        password=input('Enter the password :')
        with open('registeration.json','r') as f:
            self.register=json.load(f)
        if email_id not in self.register:
            print('Invalid Email Id or password OR You are new user. Please register')
        else:
            if self.register[email_id]['Password']==password:
                print('***********************************Login successful***********************************')
                print('Press 1 to Place Order')
                print('Press 2 to view order history')
                print('Press 3 to update profile')
                choice=int(input('Enter your choice :'))
                if choice==1:
                    with open('Flower.json','r') as f:
                        self.flowers_item=json.load(f)
                    for i in self.flowers_item:
                        order=('{}: {}'.format(str(i),self.flowers_item[str(i)]))
                        print(order)
                    a=list(input('Enter you id of flowers you want to buy :').split())
                    for i in a:
                        if i in self.flowers_item:
                            place_order={str(i):self.flowers_item[i]}
                            
                            self.place_order_list.append(place_order)
                    key=random.randint(1,100)
                    self.order_history[key]=self.place_order_list
                    with open('Order_history.json','w') as f:
                        json.dump(self.order_history,f,indent=4)
                    return 'Order placed successfully'
                
                elif choice==2:
                    print('Previous Order history is :')
                    with open('Order_history.json','r') as f:
                        self.order_history=json.load(f)   
                    print(self.order_history)
                
                elif choice==3:
                    print('*'*100)
                    print('Press 1 to update name')
                    print('Press 2 to update Ph number')
                    print('Press 3 to update address')
                    print('Press 4 to update Password')
                    ch1=int(input('Enter your choice you want to perform :'))
                    with open('registeration.json','r') as f:
                        self.register=json.load(f)
                    if ch1==1:
                        updated_value=input('Enter your name :')
                        self.register[email_id]['Name']=updated_value
                        with open('registeration.json','w') as f:
                            json.dump(self.register,f,indent=4)
                        print('Your updated information is :')
                        return self.register[email_id]
                    elif ch1==2:
                        updated_value=int(input('Enter your Phone number :'))
                        self.register[email_id]['Phone_no']=updated_value
                        with open('registeration.json','w') as f:
                            json.dump(self.register,f,indent=4)
                        print('Your updated information is :')
                        return self.register[email_id]
                    elif ch1==3:
                        updated_value=(input('Enter your Address :'))
                        self.register[email_id]['Address']=updated_value
                        with open('registeration.json','w') as f:
                            json.dump(self.register,f,indent=4)
                        print('Your updated information is :')
                        return self.register[email_id]
                    elif ch1==4:
                        updated_value=(input('Enter your Password :'))
                        self.register[email_id]['Password']=updated_value
                        with open('registeration.json','w') as f:
                            json.dump(self.register,f,indent=4)
                        print('Your updated information is :')
                        return self.register[email_id]
                    else:
                        print('Invalid input')
                else:
                    print('Invalid input')
            else:
                print('Invalid User')
                
