size=input("enter size of the piza:")
bill=0
if size=="small":
    bill=bill+100
    print("small pizza price is 100")
    peperoni=input("enter yes/no for peperoni")
    if peperoni=="yes":
        bill=bill+30
    print(f"total bill is {bill}")
    extra_cheese=input("enter yes/no for extra cheese")
    if extra_cheese=="yes":
        bill=bill+20
    print(f"total bill is {bill}")
    
elif size=="medium":
    bill=bill+200
    print("medium pizza price is 200")
    peperoni=input("enter yes/no for peperoni")
    if peperoni=="yes":
        bill=bill+50
    print(f"total bill is {bill}")
    extra_cheese=input("enter yes/no extra cheese")
    if extra_cheese=="yes":
        bill=bill+20
    print(f"total bill is {bill}")
else:
    size="large"
    bill=bill+300
    print("large pizza price is 300")
    peperoni=input("enter yes/no for peperoni")
    if peperoni=="yes":
        bill=bill+50
    print(f"total bill is {bill}")
    extra_cheese=input("enter yes/no for extra cheese")
    if extra_cheese=="yes":
        bill=bill+20
    print(f"total bill is {bill}")
