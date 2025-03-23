"""
14. A bank's ATM follows these rules:
a. A user can withdraw money only in multiples of 100
b. The withdrawal amount should not exceed the account balance
c. The system should deduct a 1% transaction fee on each successful withdrawal
d. If the conditions are met, print the remaining balance; otherwise, print "Transaction
Failed"
Input: Balance: 5000, Withdraw: 1300
Output: Transaction Failed
"""

balance = int(input("Enter your balance: "))
w_amt = int(input("Enter withdrawl amount: "))

txn_fee = (1 / 100) * w_amt
if w_amt % 100 == 0 and (w_amt + txn_fee) <= balance:
    balance -= w_amt + txn_fee
    print("Transaction successful\n")
    print(f"Withdrawl Amount: ₹{w_amt}")
    print(f"Txn Fee: ₹{txn_fee}")
    print(f"Remaining Balance: ₹{balance}")
else:
    print("Transaction Failed")