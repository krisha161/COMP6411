import socket

while True:
    print("Welcome to Server, Server open and listening ")
    port = 4444
    ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser.bind((socket.gethostname(),port))
    ser.listen()                                                    # always listening

    student_dic={}
    student_file = open("student", "r")     # student file
    for student in student_file.readlines():
        student=student.lower()
        temp=student.split("|")
        if temp[0].isalpha() and temp[1].isnumeric():
            student_dic.update({temp[0]:student})

    def findCustomer(x):
        if x in student_dic.keys():
            ans = student_dic.get(x)
        else:
            ans = "Customer not found"
        return ans

    def addCustomer(x):
        chec = findCustomer(x[1])
        if chec == "Customer not found":
            inp = x[1] + "|" + x[2] + "|" + x[3] + "|" + x[4] +"\n"
            student_dic.update({x[1]: inp})
            return "Customer added"
        else:
            rly="Customer with this name already exists"
            return rly


    def deleteCustomer(x):
        chec=findCustomer(x)
        if chec=="Customer not found":
            rly = "Customer with this name doesn't exists"
            return rly
        else:
            del student_dic[x]
            ans = "Customer Deleted"
            return ans

    def updateAge(x,y):
        ans1 = findCustomer(x)
        if ans1 == "Customer not found":
            rly="Customer with this name doesn't exists"
            return rly
        else:
            temp = student_dic.get(x).split("|")
            temp[1]=y
            inp=temp[0]+"|"+temp[1]+"|"+temp[2]+"|"+temp[3]
            student_dic.update({x:inp})
            ans = "Customer's Age Updated"
            return ans

    def updateAdr(x,y):
        ans1 = findCustomer(x)
        if ans1 == "Customer not found":
            rly = "Customer with this name doesn't exists"
            return rly
        else:
            temp = student_dic.get(x).split("|")
            temp[2] = y
            inp = temp[0] + "|" + temp[1] + "|" + temp[2] + "|" + temp[3]
            student_dic.update({x: inp})
            ans = "Customer's Address Updated"
            return ans

    def updatePhn(x,y):
        ans1 = findCustomer(x)
        if ans1 == "Customer not found":
            rly = "Customer with this name doesn't exists"
            return rly
        else:
            temp = student_dic.get(x).split("|")
            temp[3] = y
            inp = temp[0] + "|" + temp[1] + "|" + temp[2] + "|" + temp[3] +"\n"
            student_dic.update({x: inp})
            ans = "Customer's Phone number Updated"
            return ans

    def printReport():
        ans=""
        for key in sorted(student_dic.keys()):
            ans = ans + student_dic.get(key)
        return ans

    client , addr = ser.accept()                                        # bind server to client
    try:
        while True:
            reply=client.recv(1024)                                          # reciveing requent from client
            act=reply.decode().split(",")
            act[1]=act[1].lower()
            if act[0]== "find":
                m=findCustomer(act[1])
                client.send(bytes(str(m),"utf-8"))
                continue

            elif act[0]== "add":
                m = addCustomer(act)
                client.send(bytes(str(m), "utf-8"))
                continue

            elif act[0] == "delete":
                m=deleteCustomer(act[1])
                client.send(bytes(str(m), "utf-8"))
                continue

            elif act[0]== "updateAge":
                m = updateAge(act[1],act[2])
                client.send(bytes(str(m), "utf-8"))
                continue

            elif act[0]== "updateAdr":
                m = updateAdr(act[1], act[2])
                client.send(bytes(str(m), "utf-8"))
                continue

            elif act[0]== "updatePhn":
                m = updatePhn(act[1], act[2])
                client.send(bytes(str(m), "utf-8"))
                continue

            elif act[0]== "printReport":
                m = printReport()
                client.send(bytes(str(m), "utf-8"))
                continue
            else:
                break
    except:
        continue