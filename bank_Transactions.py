from multiprocessing import Pool, Lock, Value, Process
import multiprocessing.dummy as mp
import time
import random
import string

class Bank_Transactions:
    max_value_of_transactions = 50000 # Total amount of credits and debits combined
    total_value_of_transactions = 0
    total_number_of_transactions_possible = 50000

    def init(self, args):
        ''' store the counter for later use '''
        global total_value_of_transactions
        total_value_of_transactions = args


    def __init__(self):
        self.amount_in_account = 1000

def amount_debit(input_object):
    global total_value_of_transactions

    # object_to_exercise = input_object.Id
    current_transaction_amount = random.randint(100, 200)

    if Bank_Transactions.total_number_of_transactions_possible > 0 and (total_value_of_transactions.value) < \
            Bank_Transactions.max_value_of_transactions:
        time.sleep(3)
        with total_value_of_transactions.get_lock():
            if input_object.amount_in_account > current_transaction_amount:
                print("Debiting %s amount from account of %s" % (current_transaction_amount, input_object.Id))
                input_object.amount_in_account = input_object.amount_in_account - current_transaction_amount
                print("total amount in %s is :%s" % (input_object.Id, input_object.amount_in_account))
                Bank_Transactions.total_number_of_transactions_possible -= 1

                total_value_of_transactions.value += current_transaction_amount
                print("TOTAL VALUE %s" % (total_value_of_transactions.value))
            else:
                print("Cannot debit %s amount from account of %s due to shortage of funds" % (current_transaction_amount, input_object.Id))
    else:
        if total_value_of_transactions.value > Bank_Transactions.max_value_of_transactions:
            print("total value of transactions exceeded limit. Exiting")
            exit(0)

        print("Transactions limit exceeded per day for %s" % input_object.Id)

def amount_credit(input_object):
    global total_value_of_transactions

    current_transaction_amount = random.randint(100, 200)
    if Bank_Transactions.total_number_of_transactions_possible > 0 and (total_value_of_transactions.value) < \
            Bank_Transactions.max_value_of_transactions:
        time.sleep(1)
        with total_value_of_transactions.get_lock():
            print("Crediting %s amount from account of %s" % (current_transaction_amount, input_object.Id))
            input_object.amount_in_account = input_object.amount_in_account + current_transaction_amount
            print("Total amount in %s is :%s" % (input_object.Id, input_object.amount_in_account))
            Bank_Transactions.total_number_of_transactions_possible -= 1

            total_value_of_transactions.value += current_transaction_amount
            print("TOTAL VALUE %s" % (total_value_of_transactions.value))
    else:
        if total_value_of_transactions.value > Bank_Transactions.max_value_of_transactions:
            print("total value of transactions exceeded limit. Exiting")
            exit(0)

        print("Transactions limit exceeded per day for %s" % input_object.Id)

    def amount_debit_atm(self, amount_to_be_debited):

        print("Debiting %s amount from account via ATM %s")
        amount_in_account = amount_in_account - amount_to_be_debited

    def account_number_assign(self, input_customer_number):
        return "Bank" + input_customer_number

    def select_type_of_transaction(self):
        type_of_transaction = [self.amount_credit, self.amount_debit]
        return random.choice(type_of_transaction)

if __name__ == '__main__':

    # Creation of 100 customers
    number_of_customers = 5
    custocount = 0
    max_value_of_transactions = 100000000
    total_value_of_transactions = Value('i', 0)
    m1 = Bank_Transactions()

    # Initialize same class for all the customers
    objs = [Bank_Transactions() for i in range(number_of_customers)]
    print("list is %s" %objs)

    # Initialize Customer details
    for customer in objs:
        custocount+=1
        customer.Name = ''.join(random.choice((string.ascii_letters)) for i in range(random.randint(5, 20))) #Generating random name between 5,20 char
        customer.Id = 'customer_' + str(custocount)
        customer.age = random.randint(18,100)

    number_of_parallel_transactions = 4

    while(1):
        p = mp.Pool(initializer=m1.init, initargs=(total_value_of_transactions,))
        credit_or_debit = random.choice([1, 2])
        if credit_or_debit == 1:
            p.map(amount_debit, random.sample(objs,random.randint(0,3)))
        else:
            p.map(amount_credit, random.sample(objs, random.randint(0,3)))
        p.close()
        p.join()
        print("============================================================")

























    # procs = [Process(target=transaction_operation_function, args=(objs[i], act_counter)) for i in range(0,10)]
    #
    # for p in procs: p.start()
    # for p in procs: p.join()
    # while 1:
    #     list(map(transaction_operation_function, objs))
    # transaction_operation_function(objs[1])
    # transaction_operation_function(objs[2])
    # transaction_operation_function(objs[1])
