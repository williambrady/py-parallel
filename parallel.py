#!/usr/bin/env python3
#
# Test a parallel execution
#
#########
#
#   Load Accounts
#   loop: auth, deploy mp from queue
#
#########
import multiprocessing as mp
import os
import random

batch_size = 4

def load_account_list(accounts):
    # Array of things to load into the full queue
    # print('Setting up account queue')
    ct = 1
    for account in accounts:
        print('\tLOAD account ',ct, ' : ', account)
        account_queue.put(account)
        ct += 1

def executive_function(account):
    # Build the command
    run_it = f"echo docker the account {account} with some other info {account} for \\\"sure\\\""
    rand_sleep = f"sleep {random.randint(1, 20)}"
    # Execute the command
    # print(run_it)
    os.system(run_it)
    # print(rand_sleep)
    os.system(rand_sleep)

def job_manager():
    objects_done = int(wave_count) * int(batch_size)
    total_objects = len(accounts)
    text = f"figlet -w 200 Job Manager Wave : {wave_count} : {objects_done} / {total_objects}"
    os.system(text)

    # Authenticate to ensure tokens are valid
    auth()

    # Build a small batch of commands to run in parallel.
    for x in range (batch_size):
        if not account_queue.empty():
            qbert = account_queue.get()
            print('\tPREP Deployment for ', qbert)
            process = mp.Process(target=executive_function, args=(qbert,))
            process.start()
            
    #    else:
    #        print('DEBUG: Queue dried up.')
    # After the whole batch has executed, join the process to allow them to complete.
    process.join()

def auth():
    print('\nAUTH: insert process to check-out credentials')


if __name__ == '__main__':

    os.system("figlet -w 200 Beginning account deployment")
    os.system("date")

    # Create the Queue
    account_queue = mp.Queue()

    # Load accounts into a queue
    accounts = ['prd-one', 'prd-two', 'prd-three', 'prd-four', 'prd-five', 'prd-six', 'prd-seven', 'prd-eight', 'prd-nine']
    # accounts = os.listdir(environment/././)
    load_account_list(accounts)

    # Count iterations
    wave_count = 0
    # If the account_queue is empty, stop everything
    while not account_queue.empty():
        wave_count += 1
        job_manager()

    # All done!
    # print("Run complete.")
    os.system("figlet -w 200 Run Complete")
    os.system("date")
    