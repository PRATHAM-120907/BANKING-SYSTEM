accounts =  {}
def create_account(account_number , holders_name , balance):
    accounts[account_number] = {
        'holders_name' : holders_name,
        'balance' : balance
    }
    print(f"ACCOUNT{account_number} CREATED FOR {holders_name} WITH BALANCE {balance}")

def deposit(account_number , amount):
    if account_number in accounts:
        accounts[account_number]['balance']+=amount
        print(f"DEPOSITED {amount} IN ACCOUNT{account_number}")
    else:
        print("ACCOUNT NOT FOUND ")


def withdraw(account_number , amount):
    if account_number in accounts:
        if accounts[account_number]['balance']>=amount:
            accounts[account_number]['balance']-=amount
            print(f"WITHDRAW{amount} FROM ACCOUNT{account_number}")
        else:
            print("INSUFFICIENT BALANCE")
    else:
        print("ACCOUNT NOT FOUND")
            
def display_account(account_number):
    if account_number in accounts:
        print(f"ACCOUNT NUMBER : {account_number}")
        print(F"HOLDERS NAME :{accounts[account_number]['holders_name']}")
        print(f"BALANCE:{accounts[account_number]['balance']}")
    else:
        print("ACCOUNT NOT FOUND ")


# Example Usage
create_account(101, "Pratham", 1000)
display_account(101)
deposit(101, 500)
withdraw(101, 300)
display_account(101)