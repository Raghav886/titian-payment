class User:
    pur=[]
    def __init__(self,username,password,phno,address):
        self.username=username
        self.password=password
        self.phno=phno
        self.address=address
    def uploadPurchase(self):
        day=input(("Enter Purchase Day"))
        month=input(("Enter Purchase Month"))
        year=input(("Enter Purchase Year"))
        card=input("Enter Card")
        amount=input("Enter Amount Paid")
        pur.append(Purchase(day,month,year,card,amount,False))

    def gettotalDue(self):
        x=0
        for i in pur:
            x+=pur.total()
        return x
    
    


    