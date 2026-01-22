class budget:
    def __init__(self):
        self.__items=""
        self.__price=0
        self.__record=[]
        self.menu()

    def menu(self):
        try:
            x=int(input("""
                    1)click 1 for input detais
                    2)click 2 for get details(normal)
                    3)click 3 for store in text file
                    4)click 4 to end:"""))
        except Exception as e:
            print(e)
        
        if(x==1):
            self.set_details()
        elif(x==2):
            self.get_details()
        elif(x==3):
            self.store_in_txt()
        else:
            print("thank you!!!")
    

    def set_details(self):
        self.__items=input("enter your item:")
        self.__price=int(input("enter your price:"))
        self.__record.append((self.__items,self.__price))
        self.menu()
    def get_details(self):
        total_price=0
        for item,price in self.__record:
            total_price=total_price+price
            print(item,"--->",price)
        print("\ntotal Price:",total_price)
        self.menu()
    def store_in_txt(self):
         total_price=0
         with open("1_Project_expense/expense.txt", "a") as file:
            for item, price in self.__record:
                file.write(f"{item} ---> {price}\n")
                total_price=total_price+price
            file.write(f"        total price:{total_price}\n")
    
if __name__=="__main__":
    budget()
