balance=50
while balance>0:
    print(f"Amount Due: {balance}")
    paid_amount=int(input("Please pay"))
    if paid_amount in [5,10,25]:
        balance=balance-paid_amount
print(f"Change Owed: {-balance}")



