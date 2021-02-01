import time, datetime

path = 'C:\Users\jadu900142\Documents\csp_py/teet_t1_t2.txt'

Set_Temp = [35, 40, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 65, 70, 75, 80]

Wth = "D_BoilHTset"
D_Set = "D_T2L_HTset"

def Temp_test(SetTemp, DSet, Watch, txtpath) :
    hexdecimal = WatchOption.Hexdecimal
    debugger_watch_get = 0
    delay = 1
    for i in SetTemp :
        f = open(txtpath, 'a')
        f.write(str(datetime.datetime.now())+', '+'SET: , '+str(i)+'\n')
        debugger.Watch.SetValue(str(DSet), i)
        
        while debugger_watch_get != i :
            debugger_watch_get = int(debugger.Watch.GetValue(str(Watch), hexdecimal))

        f.write(str(datetime.datetime.now())+', '+'Watch: , '+str(debugger_watch_get)+'\n')
        f.close()
        
        time.sleep(delay)


Temp_test(Set_Temp, D_Set, Wth, path)