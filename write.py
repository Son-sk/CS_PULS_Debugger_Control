import time, datetime

def convertBase(number, base): # convert format
    T="0123456789ABCDEF"
    i,j=divmod(number,base)
    if i==0:
        return T[j]
    else:
        return convertBase(i,base)+T[j]

hexdecimal = WatchOption.Hexdecimal
variable = ["M_SWStep", "M_OpStep", "D_BoilHTset", "D_BoilWTset", "D_RCRTset", "D_RCHTset", "D_RCWTset"]
variable_hex = ["M_SWStep", "M_OpStep"]
path = 'C:\Users\jadu900142\Documents\csp_py/new.txt'
delay = 0.5

f = open(path, 'a')
i=0
data = str(datetime.datetime.now())+', '
for i in variable :
    data += i+', '
f.write(data+'\n')

f.close()

while(True) :
    time.sleep(delay)
    f = open(path, 'a')

    i=0
    data = str(datetime.datetime.now())+', '
    for i in variable :
        debugger_watch_get = int(debugger.Watch.GetValue(i, hexdecimal))
        if i in variable_hex :
            debugger_watch_get_16 = convertBase(debugger_watch_get, 16)
            data += str(debugger_watch_get_16)+', '   
        else : 
            data += str(debugger_watch_get)+', '
            
    f.write(data+'\n')
    f.close()
