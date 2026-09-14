from backend import CATPoffline
#The clint
from time import sleep
b = CATPoffline()

inpt = input("enter the cource of action:")
if inpt == 'play':
    inpt2 =input("join/host:")
    if inpt2 =="join":
        lis = b.Radar(10)
        print (lis)
        inpt3=input("enter which to joun:")
        b.request(inpt3)
        sleep(3)
        b.tcpConc(inpt3)
    elif inpt2 =='host':
        b.brodcast(b'wanaplay')
        l=b.Radar(3)
        for i in l:
            if l[i] == b'iwanaplay':
                b.tcpCons