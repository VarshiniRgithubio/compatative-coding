#exercise1
is_hot=False
is_cold=False
if is_hot:
    print("its hot day drink plenty of water")
elif is_cold:
    print("its cold day wear warm cloths")
else:
    print("lovely day")
print("enjoy your day")
#exercise2
price=1000000
has_credits=False
if has_credits:
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(f"down payment:{down_payment}")
#exercise 3 and operator
income=True
credit=False
if  income and credit:
    print("eligible for loan ")
else:
    print("not eligible loan")
#or operator
income=True
credit=False
if  income or credit:
    print("eligible for loan ")
else:
    print("not eligible loan")
#not operator
credit=True
criminal=True
if  credit and not criminal:
    print("eligible for loan ")
else:
    print("not eligible loan")
#comparsion operator
temp=25
if temp>30:
    print("its hot day")
elif temp<10:
    print("its cold day")
else:
    print("nither be cold nor hot")

