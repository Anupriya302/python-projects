import random
names=["rajesh","anu priya","prakarsha","abhiram","shyamala","rakesh"]
pickup_name=random.choice(names)
print(pickup_name)
print(f"{pickup_name} will the pay bill ")

#string method split
text="welcome to jenny lectures"
splited_text=text.split('e')
print(splited_text)

import random
namess=input("enter names seperated by commas")
names=namess.split(',')
bill_payer=random.choice(names)
print(f"{bill_payer} will pay the bill")