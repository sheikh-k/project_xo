from ast import literal_eval
from backend import CATPoffline,Playground
#the server
a = CATPoffline()
from time import sleep
inpt = input("enter the cource of action:")
if inpt == 'play':
    inpt2 =input("join/host:")
    if inpt2 =="join":
        lis = a.Radar(1)
        print (lis)
        inpt3=input("enter which to joun:")
        a.request(inpt3)
        sleep(0.5)
        a.tcpConc(inpt3)
        pg1 = Playground()
        while True:
            message = literal_eval(a.get().decode())
            if message[0] == 'won':
                print(message[1], 'won')
                break

            move, by = message
            pg1.moveinput(move,by)
            print(pg1)
            inpt5m, by5 = literal_eval(input("Enter move, e.g. ([0, 0], 'X'): "))
            pg1.moveinput(inpt5m,by5)
            flag = pg1.check()
            if flag:
                a.send(repr(('won', flag)).encode())
                print(flag,'won')
                a.endCon()
                break
            a.send(repr((inpt5m, by5)).encode())
    elif inpt2 =='host':
        a.brodcast(b'wanaplay')
        l=a.Radar(0.0001)
        for i in l:
            if l[i] == b'iwanaplay':
                a.tcpCons()
                pg2 = Playground()
                print(pg2)
                inpt4m, by4 = literal_eval(input("Enter move, e.g. ([0, 0], 'X'): "))
                pg2.moveinput(inpt4m, by4)
                flag = pg2.check()
                if flag:
                    a.send(repr(('won', flag)).encode())
                    print(flag,'won')
                    a.endCon()
                    break

                a.send(repr((inpt4m, by4)).encode())
                while True:
                    message = literal_eval(a.get().decode())
                    if message[0] == 'won':
                        print(message[1], 'won')
                        break

                    move, by = message
                    pg2.moveinput(move,by)
                    print(pg2)
                    inpt4m, by4 = literal_eval(input("Enter move, e.g. ([0, 0], 'X'): "))
                    pg2.moveinput(inpt4m,by4)
                    flag = pg2.check()
                    if flag:
                        a.send(repr(('won', flag)).encode())
                        print(flag,'won')
                        a.endCon()
                        break
                    a.send(repr((inpt4m, by4)).encode())