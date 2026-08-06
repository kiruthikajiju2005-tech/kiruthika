n=int(input("enter the value:"))
nrev=0
while(n!=0):
    r=n%10
    nrev=(nrev*10)+r
    n//=10

print("rverse digit=",nrev)    
