balance=100000
user=int(input("Enter 0 for withdraw and 1 for deposit"))
if user==1:
    amount=int(input("Enter amount to be deposited : "))
    balance+=amount
    print("Amount deposit and balance is Rs.",balance)
elif user==0:
    amount=int(input("Enter amount to be withdraw : "))
    if amount<=balance:
        balance-=amount
        print("Amount withdraw and balance is Rs.",balance)
    else:
        print("Insufficient Fund")
