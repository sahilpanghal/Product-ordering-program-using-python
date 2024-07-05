def Stat():
    try:
        stats=open("statistics.txt","r")
        data=stats.read()
        print(data)
    except:
        print("\nNo orders\n")
    
    
def AddProduct():
    while True:
        try:
            prod=open("Product","r")
            product=prod.readlines()
            prod.close()
            break
        except FileNotFoundError:
            prod=open("Product","a")
            prod.close()
    prod=open("Product","a")
    name=input("Enter the Product name ")
    price=input("Enter the price ")
    try:
        data=str(int(product[len(product)-2][0])+1)+") "+name+"\n"+price+"\n"
    except:
        data="1) "+name+"\n"+price+"\n"
    prod.write(data)
    prod.close()
    

while True:
    print("Main Menu\n")
    print("    Press 1 to see statistics")
    print("    Press 2 to add Product")
    print("    Press 0 to quit\n")
    ch=int(input("Enter your choice  "))
    if ch==1:
        Stat()
    elif ch==2:
        AddProduct()
    elif ch==0:
        break
    else:
        print("Invalid choice")
