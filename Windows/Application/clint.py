

def validate(string):
    returnT = [1,1]
    if len(string) < 4:
        returnT[0] = 0
    if not string.remove('_').isalnum():
        returnT[1] = 0
        
        
        
ERRORCODE = {
    1:' too short',
    2:' can only contain alpahbets ,numbers and underscors',
    3:' username and password cant be same'
    
}
        

def register(username,password):
    if username == password:
        pass
        
    C1 = validate(username)
    C2 = validate(password)
    
        