size=input("enter size of the shawarma:")
price=0
if size=="small":
    price=100
    print("small shawarma price is 100")
    fresh_cream=input("for fresh cream enter yes/no")
    if fresh_cream=="yes":
        price=price+10
    print(f"price of small shawarma is {price}")
    extra_spice=input("for extra spice enter yes/no")
    if extra_spice=="yes":
        price=price+10
    print(f"total price of small shawarma{price}")
if size=="medium":
    price=200
    print("mediium shawarma price is 100")
    fresh_cream=input("for fresh cream enter yes/no")
    if fresh_cream=="yes":
        price=price+20
    print(f"price of medium shawarma is {price}")
    extra_spice=input("for extra spice enter yes/no")
    if extra_spice=="yes":
        price=price+20
    print(f"total price of medium shawarma{price}")
if size=="large":
    price=300
    print("large shawarma price is 100")
    fresh_cream=input("for fresh cream enter yes/no")
    if fresh_cream=="yes":
        price=price+30
    print(f"price of large shawarma is {price}")
    extra_spice=input("for extra spice enter yes/no")
    if extra_spice=="yes":
        price=price+30
    print(f"total price of large shawarma{price}")




