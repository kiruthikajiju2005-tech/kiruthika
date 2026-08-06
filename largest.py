a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter c value"))
if a>b and a>c:
    large=a
elif b>c:
    large=b
else:
    large=c
print("Largest value is ",large)
