import time, datetime

def convertBase(number, base): # convert format
    T="0123456789ABCDEF"
    i,j=divmod(number,base)
    if i==0:
        return T[j]
    else:
        return convertBase(i,base)+T[j]

hexdecimal = WatchOption.Hexdecimal
variable = ["D_Hour", "D_Minute", "D_RTC.Hour", "D_RTC.Minute", "D_RTC.Second"]
variable_val = [0,0,0,0,0]
today = datetime.datetime.now()
filename = today.strftime("%Y%m%d")+'.txt'
path = 'C:\Users\jadu900142\Documents\csp_py/'+filename
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
    i=0
    j=0
    flag = 0
    data = str(datetime.datetime.now())+', '
    for i in variable :
        debugger_watch_get = int(debugger.Watch.GetValue(i, hexdecimal))
        if i == variable[j] :
            if j >= 2 :
                debugger_watch_get = convertBase(debugger_watch_get, 16)
            else :
                pass
            if variable_val[j] != debugger_watch_get :
                variable_val[j] = debugger_watch_get
                flag = 1
        j+=1

    i=0
    if flag == 1 :
        for i in variable_val :    
            data += str(i)+', '
        f = open(path, 'a')
        f.write(data+'\n')
        f.close()
