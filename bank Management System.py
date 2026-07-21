import pymysql

connect=pymysql.connect(
    host='localhost',
    user='root',
    password='xxxx',
    database='bank'
    )

cursor = connect.cursor()

def create_account(account_no,name,balance):
    try:
        sql='insert into account_detail(account_no,name,balance) values (%s,%s,%s)'
        cursor.execute(sql,(account_no,name,balance))
        connect.commit()
        print('Account created successfully!')
    except Exception as e:
        print('Error:',e)

def view_accounts():
    cursor.execute('select*from account_detail')
    account_detail=cursor.fetchall()
    for acc in account_detail:
        print(acc)

def deposit(account_no,amount):
    sql='UPDATE account_detail SET balance = balance + %s WHERE account_no=%s'
    cursor.execute(sql,(amount,account_no))
    connect.commit()
    print('Amount deposited successfully')

def withdraw(account_no,amount):
    cursor.execute('SELECT balance FROM account_detail WHERE account_no=%s',(account_no,))
    result=cursor.fetchone()
    if result:
       balance=result[0]
       if balance>=amount:
           sql='UPDATE account_detail SET balance = balance - %s WHERE account_no=%s'
           cursor.execute(sql,(amount,account_no))
           print('withdrawal  Successful!')
       else:
           print('Insufficient balance!')
    else:
        print('Account not found!')

def check_balance(account_no):
    cursor.execute('select*from account_detail WHERE account_no=%s',(account_no,))
    result=cursor.fetchone()
    if result:
        print(result)
    else:
        print('Account not found!')
    
def delete_account(account_no):
    cursor.execute('DELETE FROM account_detail WHERE account_no=%s',(account_no,))
    connect.commit()
    print('Account deleted Successfull!')

while True:
    print('\n BANK MANAGEMENT SYSTEM')
    print('1.Create Account')
    print('2.View Account Detail')
    print('3.Deposit')
    print('4.Withdraw')
    print('5.Check Balance')
    print('6.Delete Account')
    print('7.Exit')

    choice=input('Enter your choice (1-7):')

    if choice=='1':
        acc=int(input('Enter account number:'))
        name=input('Enter name:')
        bal=float(input('Enter  initial balance:'))
        create_account(acc,name,bal)
        
    elif choice=='2':
        view_accounts()

    elif choice=='3':
        acc=int(input('Enter account number:'))
        amt=float(input('Enter amount:'))
        deposit(acc,amt)

    elif choice=='4':
        acc=int(input('Enter account number:'))
        amt=float(input('Enter amount:'))
        withdraw(acc,amt)

    elif choice=='5':
        acc=int(input('Enter account number:'))
        check_balance(acc)

    elif choice=='6':
        acc=int(input('Enter account number:'))
        delete_account(acc)

    elif choice=='7':
        print('Exiting...')
        break

    else:
        print('Invalid choice!')
                  
              
    
    
    
