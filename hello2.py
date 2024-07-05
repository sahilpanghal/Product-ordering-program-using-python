
#login form
import pickle
import os
import random
import getpass
import re



def binread(file):  
    # read data of a binary file and store it in a list like readlines() for txt file
    l=[]
    while True:     
    # read each line by pickle.load() till last line of file is reached 
        try:
            l.append(pickle.load(file))
        except:
            break
        # except break infinite loop when there is no further line to read
    for i in range(len(l)):
        l[i]=l[i].split("\n")
        # seperate each line by splitting with \n
    return(l)


def lsearch(list,item):
    # linear search
    for i in range(0,len(list)):
        if list[i].rstrip("\n")==item:
            return i
    return -1

def mailcheck(email):
    # check that email used while signup already exist
    information = open("Information.txt","rb")
    inf = binread(information)
    status=0
    for i in range(len(inf)):
        if inf[i][2]==email.rstrip("\n"):
            status=1       
    # status=1 if email already exist else status=0
    return(status)


def check(email):
    # check whether email is like ' ___@___.___'
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex,email)):  
        return 1
          
    else:  
        return 0


def contactcheck(contact):
    # check whether the length of contact is 10 i.e valid or not
    if len(contact.rstrip("\n"))==10:
        return 1
    else:
        return 0
    


def passcheck():
    # check whether password contains a digit,special symbol($,%,@) and have upto 8 character
    password=getpass.getpass("Password--> ")
    
    digit=0
    symbol=0
    
    for i in password:
        if i in "1234567890":
            digit+=1
        elif i in "@$%":
            symbol+=1
            
        # if digit found add 1 to digit and same for special symbol
        # if atleast 1 digit and 1 special symbol found break loop and return 1 in digit
        
        if digit>=1 and symbol>=1:
            digit=1
            break
        
    if digit!=1 and len(password)<9:
        print("Password must contains a digit,special symbol($,%,@) and must have upto 8 character") 
        return(passcheck())
    else:
        return(password)



def Signup():
    information = open("Information.txt","ab")
    name = input("Name--> ")+"\n"
    while True:
        contact = input("Contact--> ")+"\n"
        if contactcheck(contact)==1:
            break
        else:
            print("Invalid Contact")
            
    while True:
        email = input("Email id--> ")+"\n"
        if mailcheck(email)==0:
            if check(email)==1:
                break
            else:
                print("Invalid email")
        else:
            print("Email already exist\n")
        
        
    
    password = passcheck()
    inf = name+contact+email+password
    
    pickle.dump(inf,information)
    information.close()


def Validation():
    information = open("Information.txt","rb")
    inf = binread(information)
    
    index=-1
    
    while True:
        email = input("Email id--> ")
        password = getpass.getpass("Password--> ")
        for i in range(len(inf)):
            if inf[i][2]==email and inf[i][3]==password:
                # check authenticity of email and password
                index=i
                break
           
        if index==-1:
            print("Invalid credidentials\n")
        else:
            print("Login successful\n")
            user.append(inf[index][2])
            # add the email of user signed in in a list in __main__ for further use
            break
    return(inf[index][0])
    information.close()
        

def Login():
    index=Validation()
    if index!=None:
        print("Welcome",index," to Redcart\n")
        
def Logout():
    # delete the email of user currently login from user list
    user.pop()
        
    
def Products():
    product=open("Product","r")
    list=product.readlines()
    for i in range(0,len(list),2):
        print(list[i],"Rs",list[i+1])
    # give all the products available
    
    ch=input("Enter your choice ")
    for i in range(0,len(list),2):
        if list[i][0]==ch:
            choice=list[i][3:]
            price="Rs "+list[i+1]
            break
    # take input of item user want to add to cart
    return(choice,price,"1"+"\n")
    product.close()
    
    
def MyOrder():
    # read and print all prevous orders of user
    try:
        print("\n")
        myorder=open(user[0]+"'s order.txt","r")
        print(myorder.read())
    except:
        print("No orders yet")
    # if no orders, to prevent crash ,except print no orders
    
def AddToCart():
    prod=Products()
    prod=list(prod)
    # prod get details(name,price,quantity) of selected product
    while True:
        try:
            cart=open(user[0]+".txt","r")
            item=cart.readlines()
            cart.close()
            break
        except FileNotFoundError:
            cart=open(user[0]+".txt","a")
            cart.close()
   # create a cart by except if no cart exist
    index=-1
    for i in range(len(item)):
        if item[i]==prod[0]:
            index=i
    if index!=-1:
        item[index+2]=str(int(item[index+2])+1)+"\n"
    else:
        try:
            item[0]!=None
            item.extend(prod)
        except:
            item=prod
    
    newcart=open("temp1.txt","a")
    for i in range(len(item)):
        newcart.write(item[i])
    newcart.close()
    print("\n"+prod[0].rstrip("\n"),"added successfully")
    os.remove(user[0]+".txt")
    os.rename("temp1.txt",user[0]+".txt")
    # add product details to cart
    # open a connection to temporary file and write all previous cart item and new item details in that file
    # then delete previous cart and rename temporary file to previous cart name
    

def Delete():
    # delete any product from cart
    try:
        print("\nItems in your cart are")
        Cart()
        cart=open(user[0]+".txt","r")
        item=cart.readlines()
        delete=input("Enter the name of product you want to delete ")
        newcart=open("temp.txt","a")
        for i in range(0,len(item),3):
            if item[i].lower().rstrip("\n")==delete.lower():
                if int(item[i+2])==1:
                    pass
                else:
                    newcart.write(item[i]+item[i+1]+str(int(item[i+2])-1)+"\n")
            else:
                newcart.write(item[i]+item[i+1]+item[i+2])
        cart.close()
        newcart.close()
        newcart=open("temp.txt","r")
        if newcart.readlines()!=[]:
            newcart.close()
            os.remove(user[0]+".txt")
            os.rename("temp.txt",user[0]+".txt")
        else:
            newcart.close()
            os.remove(user[0]+".txt")
            os.remove("temp.txt")

    except:
        pass
    # open a connection to temporary file and write all cart item in that file except the one to delete
    # then delete previous cart and rename temporary file to previous cart name

def Cart():
    try:
        cart=open(user[0]+".txt","r")
        item=cart.readlines()
        print("\n")
        for i in range(0,len(item),3):
            print(item[i]+item[i+1]+"Quantity--> ",item[i+2])
        cart.close()
    except:
        print("\nYour Cart is yet Empty")
    
    
    
def PlaceOrder():
    print("\nItems in your cart are")
    Cart()
    
    address=input("Enter your address ")
    city=input("Enter your city ")
    pincode=input("Enter pincode ")
    state=input("Enter the state ")
    
    print("To checkout press 1")
    ch=input("Enter your choice ")
    if ch=='1':
        print("Order placed successfully")
        odid=random.randint(10000,15000)
        print("Your order id is",odid,"\n")
        print("Order will be delivered to\n",address,"\n",city,",",pincode,"\n",state)
        
        while True:
            try:
                stats=open("statistics.txt","r")
                stat=stats.readlines()
                stats.close()
                break
            except FileNotFoundError:
                stats=open("statistics.txt","a")
                stats.close()
                
        temp=open("temp.txt","a")
        cart=open(user[0]+".txt","r")
        myorder=open(user[0]+"'s order.txt","a")
        item=cart.readlines()
        item.append("Order id--> "+str(odid)+"\n\n")
        
        for i in range(len(item)):
            myorder.write(item[i])
        stat.extend(item)
        
        for i in range(len(stat)):
            temp.write(stat[i])
            
        myorder.close()
        stats.close()
        cart.close()
        temp.close()
        
        os.remove("statistics.txt")
        os.rename("temp.txt","statistics.txt")
        os.remove(user[0]+".txt")
        
    else:
        print("Invalid choice")
        
    
user=[]



#__main__
while True:
    print("\nMain Menu\n")
    try: 
        user[0]==None
        print("    Press 1 to Add Items To Cart")
        print("    Press 2 to View Your Cart")
        print("    Press 3 to Order")
        print("    Press 4 to Delete Item From Cart")
        print("    Press 5 to See Your Orders")
        print("    Press 6 to Logout")
        print("    Press 0 to Quit\n")
        ch=input("Enter your choice ")
        if ch=='1':
            AddToCart()
        elif ch=='2':
            Cart()
        elif ch=='3':
            PlaceOrder()
        elif ch=='4':
            Delete()
        elif ch=='5':
            MyOrder()
        elif ch=='6':
            Logout()
        elif ch=='0':
            break
        else:
            print("Invalid choice \n")

    except:
        print("    Press 1 for Signup")
        print("    Press 2 for Login")
        print("    Press 0 to Quit\n")
        
        ch=input("Enter your choice ")
        if ch=='1':
            Signup()
        elif ch=='2':
            Login()
        elif ch=='0':
            break
        else:
            print("Invalid choice \n")

