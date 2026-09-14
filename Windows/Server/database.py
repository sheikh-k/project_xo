from Windows.Protocal.CATP import sockPipe
import pymysql
import sys

pipe = sockPipe()
Data = pipe.pull(('localhost',9999))
print(Data)
sys.exit(0)

CONNECTION = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'maomao09_codecat08',
    database = 'mai',
    cursorclass=pymysql.cursors.SSDictCursor
)
CURSOR = CONNECTION.cursor()


    

    