from socket import (socket ,AF_INET,SOCK_STREAM)

class CATPServer:
    def __init__(self,SIP_P,Listening=1):
        self.sock = socket(AF_INET,SOCK_STREAM)
        self.sock.bind(SIP_P)
        self.sock.listen(Listening)
        
    def manageRequest(self):
        self.con,self.add = self.sock.accept()
        
        
class CATPClint:
    def __init__(self,SIP_SP):
        self.sock = socket(AF_INET,SOCK_STREAM)
        self.SIP_SP = SIP_SP
        
    def connect(self,baseFunction):
        def modFunction(*args,**kwargs):
            self.sock.connect(self.SIP_SP)
            returnvalue = baseFunction(*args,**kwargs)
            self.sock.close()  
            return returnvalue      
        return modFunction
    
class sockPipe:
    def __init__(self):
        self.sock = socket(AF_INET,SOCK_STREAM)
        
    def push(self,host_port,Data):
        self.sock.bind(host_port)
        self.sock.listen(2)
        con , add = self.sock.accept()
        con.send(Data)  
        
    def pull(self,host_port):
        self.sock = socket(AF_INET,SOCK_STREAM)
        self.sock.connect(host_port)
        Data = self.sock.recv(1024)
        self.sock.close()
        return Data
    
        
        
    
                    

        
        
        
        