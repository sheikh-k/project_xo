from Windows.Protocal.CATP import CATPServer,sockPipe

#server = CATPServer(("localhost",7777) , Listening=10)
data = b'server said hi'
pipe = sockPipe()
pipe.push(('localhost',9999),data)


