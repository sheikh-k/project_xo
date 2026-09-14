from datetime import datetime ,timedelta

T = datetime.now()
T_formated = T.strftime('%m:%d-%I:%M %p')
print(T)
print(T_formated)
