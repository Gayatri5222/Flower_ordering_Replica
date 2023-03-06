import json 
import random
import sys
class Admin:
    def __init__(self):
        self.flowers_item={}
    def add_new_flower(self):
        self.name=input('Enter the flower name :')
        self.price=int(input('Enter the flower price :'))
        self.stock=(input('Enter the stock of plants :'))
        d={'Name':self.name, 'Price':self.price,'Stock':self.stock}
        key=random.randint(1,1000)
        self.flowers_item[key]=d
        with open('Flower.json','w') as f:
            json.dump(self.flowers_item,f,indent=4)
        return self.flowers_item
    
    def load_flower(self):
        with open('Flower.json','r') as f:
            self.flowers_item=json.load(f)
        return self.flowers_item
    
    def remove_flower(self):
        with open('Flower.json','r') as f:
            self.flowers_item=json.load(f)
        print(self.flowers_item)
        flower_key=int(input('Enter the key for which you want to remove flower :'))
        flower_key=str(flower_key)
        
        if flower_key not in self.flowers_item:
            print('Invalid Key')
            print('Enter the appropriate key')
            
        else:
            del self.flowers_item[flower_key]
            with open('Flower.json','w') as f:
                json.dump(self.flowers_item,f,indent=4)
            return self.flowers_item
        
    def edit_flower(self):
        with open('Flower.json','r') as f:
            self.flowers_item=json.load(f)
        print(self.flowers_item)
        key=int(input('Enter the key you want to edit :'))
        key=str(key)
        if key not in self.flowers_item:
            print('Invalid key')
            
        else:
            print('*'*50)
            print('Press 1 to edit Name')
            print('Press 2 to edit Price')
            print('Press 3 to edit Stock')
            ch=int(input('Enter your choice you want to edit :'))

            if ch==1:
                updated_value=input('Enter your updated value :')
                self.flowers_item[key]['Name']=updated_value
                with open('Flower.json','w') as f:
                    json.dump(self.flowers_item,f,indent=4)
                print('Your updated item is :')
                return (self.flowers_item[key])
                
            elif ch==2:
                updated_value=int(input('Enter your updated value :'))
                self.flowers_item[key]['Price']=updated_value
                with open('Flower.json','w') as f:
                    json.dump(self.flowers_item,f,indent=4)
                print('Your updated item is :')
                return (self.flowers_item[key])
            elif ch==3:
                updated_value=input('Enter your updated value :')
                self.flowers_item[key]['Stock']=updated_value
                with open('Flower.json','w') as f:
                    json.dump(self.flowers_item,f,indent=4)
                print('Your updated item is :')
                return (self.flowers_item[key])
            else:
                print('*'*50)
                print('Invalid key')
                print('Please enter the valid key to update')
                print('Thank you for visiting')
