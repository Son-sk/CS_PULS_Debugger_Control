
import time, datetime

path = 'C:\Users\jadu900142\Documents\csp_py/teet_temp.txt'
Set_HTemp = [35, 40, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 65, 70, 75, 80]
Set_RTemp = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
indoor = 1
flow = 0

Wth = "D_BoilHTset"

D_Set_Htemp = "C_SetPtr[1]"
D_Set_Rtemp = "C_SetPtr[2]"

HMode = "F_BLsts1.Bit.b4" # flow(0) or indoor(1)

def Temp_test(SetTemp, DSet, Watch, txtpath) :
    hexdecimal = WatchOption.Hexdecimal
    debugger_watch_get = 0
    delay = 1
    i=0
    for i in range(len(SetTemp)) :
        f = open(txtpath, 'a')
        f.write(str(datetime.datetime.now())+', '+str(DSet)+' SET: , '+str(i)+'\n')
        #debugger.Watch.SetValue(str(DSet), i)
        if DSet == "C_SetPtr[1]" :
            debugger.Watch.SetValue("T_ChgSetTemp[1]", 100)
        else :
            if i == 0 :
                debugger.Watch.SetValue("T_ChgSetTemp[2]", 250)
            else :
                debugger.Watch.SetValue("T_ChgSetTemp[2]", 100)

        debugger.Watch.SetValue("T_WaitLight", 200)
        debugger.Watch.SetValue(DSet, i)
        

        while debugger_watch_get != SetTemp[i] :
            debugger_watch_get = int(debugger.Watch.GetValue(str(Watch), hexdecimal))

        f.write(str(datetime.datetime.now())+', '+str(Watch)+' Watch: , '+str(debugger_watch_get)+'\n')
        if SetTemp[i] == SetTemp[len(SetTemp)-1] :
            f.write(str(datetime.datetime.now())+', '+str(Watch)+' Watch: , ''TEST OK'+'\n')    
        f.close()
        
        time.sleep(delay)

def mode_test(DSet, Mode, txtpath) :
    hexdecimal = WatchOption.Hexdecimal
    while int(debugger.Watch.GetValue(str(DSet), hexdecimal)) != Mode :
        debugger.Watch.SetValue("T_WaitLight", 200)
        debugger.Watch.SetValue("D_SwCom", 0x09)
        time.sleep(0.5)
    if Mode == 0 :
        s = "flow mode"
    else :
        s = "indoor mode"
    f = open(txtpath, 'a')
    f.write(str(datetime.datetime.now())+', '+str(DSet)+' Watch: , '+str(s)+'\n')
    f.close()



mode_test(HMode, 0, path) # flow mode

Temp_test(Set_HTemp, D_Set_Htemp, Wth, path) # flow temp

mode_test(HMode, 1, path) # indoor mode

Temp_test(Set_RTemp, D_Set_Rtemp, Wth, path) # indoor temp