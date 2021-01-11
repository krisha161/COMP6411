import socket

port=4444
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((socket.gethostname(),port))

while True:
    print("1: Find Customer")
    print("2: Add Customer")
    print("3: Delete Customer")
    print("4: Update Customer age")
    print("5: Update Customer address")
    print("6: Update Customer phone number")
    print("7: Print Report")
    print("8: Exit")

    def findCustomer():                                                             # function to find customer
        name = input("Enter the name of the customer: ")
        while True:
            if name.isnumeric() or name.isspace() or len(name) is 0:
                name = input("Enter only alphabetic names: ")
            else:
                break
        msgs="find," + str(name).lower()
        cli.send(bytes(str(msgs),"UTF-8"))                                          #sending req to server
        rly = cli.recv(1024)                                                        #recieving response from server
        print("\n"+rly.decode("UTF-8")+"\n")

    def addCustomer():                                                              # function to add customer
        name = input("Enter the name of the customer: ")
        while True:
            if name.isnumeric() or name.isspace() or len(name) is 0:
                name = input("Enter alphabetic names: ")
            else:
                break

        age = input("Enter the age: ")
        while True:
            if age.isalpha():
                age = input("Enter only numeric age: ")
            else:
                break

        adr = input("Enter the address: ")
        phn = input("Enter the phn: ")

        msgs = "add," + str(name).lower()+","+ str(age)+","+ str(adr)+"," +str(phn)
        cli.send(bytes(str(msgs), "UTF-8"))
        rly = cli.recv(1024)
        print("\n"+rly.decode("UTF-8")+"\n")

    def deleteCustomer():                                                           # function to delete customer
        name = input("Enter the name of the customer: ")
        while True:
            if name.isnumeric() or name.isspace() or len(name) is 0:
                name = input("Enter alphabetic names: ")
            else:
                break
        msgs = "delete," + str(name).lower()
        cli.send(bytes(str(msgs), "UTF-8"))
        rly = cli.recv(1024)
        print("\n"+rly.decode("UTF-8")+"\n")

    def updateAge():                                                               # function to update customer's age
        name = input("Enter the name of the customer: ")
        while True:
            if name.isnumeric() or name.isspace() or len(name) is 0:
                name = input("Enter alphabetic names: ")
            else:
                break
        age = input("Enter the age: ")
        while True:
            if age.isalpha():
                age = input("Enter only numeric age: ")
            else:
                break
        msgs = "updateAge," + str(name).lower() + "," + str(age)
        cli.send(bytes(str(msgs), "UTF-8"))
        rly = cli.recv(1024)
        print("\n"+rly.decode("UTF-8")+"\n")

    def updateAdr():                                                             # function to update customer's address
        name = input("Enter the name of the customer: ")
        while True:
            if name.isnumeric() or name.isspace() or len(name) is 0:
                name = input("Enter alphabetic names: ")
            else:
                break
        adr=input("Enter the new address: ")
        msgs = "updateAdr," + str(name).lower() + "," + str(adr)
        cli.send(bytes(str(msgs), "UTF-8"))
        rly = cli.recv(1024)
        print("\n"+rly.decode("UTF-8")+"\n")

    def updatePhn():                                                            # function to update customer's phone no.
        name = input("Enter the name of the customer: ")
        while True:
            if name.isnumeric() or name.isspace() or len(name) is 0:
                name = input("Enter alphabetic names: ")
            else:
                break
        phn = input("Enter the new phone number: ")
        msgs = "updatePhn," + str(name).lower() + "," + str(phn)
        cli.send(bytes(str(msgs), "UTF-8"))
        rly = cli.recv(1024)
        print("\n"+rly.decode("UTF-8")+"\n")

    def printReport():                                                         # function to print report
        msgs="printReport,"+"all"
        cli.send(bytes(str(msgs), "UTF-8"))
        rly = cli.recv(1024)
        print("\n"+rly.decode("UTF-8")+"\n")

    def ex():                                                                  # exit function
        print("\n Goodbye!!! \n")
        exit()

    options = {1 : findCustomer,
               2 : addCustomer,
               3 : deleteCustomer,
               4 : updateAge,
               5 : updateAdr,
               6 : updatePhn,
               7 : printReport,
               8 : ex
    }
    i=input("Enter no:")
    while True:
        if i.isalpha() or i.isspace() or len(i) is 0 or int(i)>8 or int(i)<1:
            i = input("Enter numeric number between 1 to 8: ")
        else:
            break
    options[int(i)]()