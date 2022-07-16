import time
from datetime import datetime
# pruebas de concatenacion de tiempo
dt_obj = datetime.now()
#  datetime.datetime
time.sleep(.2)
# millisec = datetime.strftime(dt_obj,'%S')s
# cuenta =lambda x:  (float(datetime.now().strftime('%S.%f')[:3]) - float(x.strftime('%S.%f')[:3]))
cuenta =lambda x:  datetime.now().strftime('%S.%f') - x.strftime('%S.%f')
print(cuenta(dt_obj))