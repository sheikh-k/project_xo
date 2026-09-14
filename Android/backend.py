from socket import socket,AF_INET,SOCK_DGRAM,SOCK_STREAM,SOL_SOCKET,SO_BROADCAST,SO_REUSEADDR,gethostname,gethostbyname
from time import time,sleep
class Playground:
    def __init__(self):
        self.ground = [[0,0,0],[0,0,0],[0,0,0]]
    def check(self):
        G = self.ground
        for i in range(3):
            if 'O' not in G[i] and 0 not in G[i]:
                return 'X'
            elif 'X' not in G[i] and 0 not in G[i]:
                return 'O'
            elif G[0][i] == G[1][i] == G[2][i] != 0:
                return G[0][i]
        else:
            if G[0][0] == G[1][1] == G[2][2] != 0:
                return G[0][0]
            elif G[0][2] == G[1][1] == G[2][0] != 0:
                return G[0][2]
        return False
    def moveinput(self,move,by):
        x = move[0]
        y = move[-1]
        if by == 'O':
            self.ground[x][y]=by
        elif by == 'X':
            self.ground[x][y]=by
        else:
            raise TypeError ('Input cant be other than X or O')
        Flag = self.check()
        return Flag
    def __str__(self):
        G = ''
        for i in self.ground:
            G+=str(i)+'\n'
        return G
    
"""
g1 = Playground()
while True:
    inpt = eval(input("Enter:"))
    state = g1.moveinput(inpt[0],inpt[-1])
    print(g1)
    if state != False:
        print(state,'Wins')
        break
"""

class CATPoffline:
    def __init__(self):
        self.myip = gethostbyname(gethostname())
    def brodcast(self,message):
        with socket(AF_INET,SOCK_DGRAM) as host:
            host.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
            host.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
            host.sendto(message,('255.255.255.255',7000))
    def Radar(self,sec):
        host = socket(AF_INET, SOCK_DGRAM)
        host.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        host.bind(("0.0.0.0",7000))
        Bl = {}
        print("Listening...")
        #Listinging for n second
        timelim = time()+sec
        while time()<=timelim:
            message, addr = host.recvfrom(1024)
            Bl[addr]=message
        return Bl
    def request(self,ip):
        with socket(AF_INET,SOCK_DGRAM) as host:
            host.sendto(b'iwanaplay',(ip,7000))
            
    def tcpCons(self):
        with socket(AF_INET,SOCK_STREAM) as server:
            server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
            server.bind(("0.0.0.0",7001))
            server.listen(1)
            self.connection, self.address = server.accept()
        
        
    def tcpConc(self,sip):
        deadline = time()+10
        while True:
            self.connection = socket(AF_INET,SOCK_STREAM)
            self.connection.settimeout(1)
            try:
                self.connection.connect((sip,7001))
                self.connection.settimeout(None)
                return
            except (ConnectionRefusedError, TimeoutError):
                self.connection.close()
                if time() >= deadline:
                    raise ConnectionError(f"Could not connect to {sip}:7001")
                sleep(0.2)
        
        
    def endCon(self):
        self.connection.close()
    def getAddress(self):
        return self.address
    def send(self,message):
        self.connection.send(message)
    def get(self):
        return self.connection.recv(1024)
