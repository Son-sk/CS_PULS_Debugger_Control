import time, datetime

def Set_heat(onoff) :
    hexdecimal = WatchOption.Hexdecimal
    if onoff == 1 :
        while debugger.Watch.GetValue("D_BoilOper", hexdecimal) != 0x30 and debugger.Watch.GetValue("D_BoilOper", hexdecimal) != 0x20   :
            debugger.Watch.SetValue("F_OneshotSw.Bit.b4", 1)
            debugger.Watch.SetValue("T_WaitLight", 200)
            time.sleep(0.5)
    else :
        while debugger.Watch.GetValue("D_BoilOper", hexdecimal) == 0x30 or idebugger.Watch.GetValue("D_BoilOper", hexdecimal) == 0x20 :
            debugger.Watch.SetValue("F_OneshotSw.Bit.b4", 1)
            debugger.Watch.SetValue("T_WaitLight", 200)
            time.sleep(0.5)


def Set_wheat(onoff) :
    hexdecimal = WatchOption.Hexdecimal
    if onoff == 1 :
        while debugger.Watch.GetValue("D_BoilOper", hexdecimal) != 0x30 and debugger.Watch.GetValue("D_BoilOper", hexdecimal) != 0x10   :
            debugger.Watch.SetValue("F_OneshotSw.Bit.b1", 1)
            debugger.Watch.SetValue("T_WaitLight", 200)
            time.sleep(0.5)
    else :
        while debugger.Watch.GetValue("D_BoilOper", hexdecimal) == 0x30 or debugger.Watch.GetValue("D_BoilOper", hexdecimal) == 0x10 :
            debugger.Watch.SetValue("F_OneshotSw.Bit.b1", 1)
            debugger.Watch.SetValue("T_WaitLight", 200)
            time.sleep(0.5)


def Set_power(onoff) :
    hexdecimal = WatchOption.Hexdecimal
    if onoff == 1 :
        while debugger.Watch.GetValue("M_SWStep", hexdecimal) == 0x00 :
            debugger.Watch.SetValue("T_WaitLight", 200)
            debugger.Watch.SetValue("D_SwCom", 0x01)
            time.sleep(0.5)
    else :
        while debugger.Watch.GetValue("M_SWStep", hexdecimal) > 0x00 :
            debugger.Watch.SetValue("D_SwCom", 0x02)
            time.sleep(0.5)

def Set_HtRapid(onoff) :
    hexdecimal = WatchOption.Hexdecimal
    if onoff == 1 :
        while debugger.Watch.GetValue("F_BLsts2.Bit.b3", hexdecimal) == 0x0 :
            debugger.Watch.SetValue("T_WaitLight", 200)
            debugger.Watch.SetValue("D_SwCom", 0x0c)
            time.sleep(0.5)
    else :
        while debugger.Watch.GetValue("F_BLsts2.Bit.b3", hexdecimal) == 0x1:
            debugger.Watch.SetValue("D_SwCom", 0x0c)
            time.sleep(0.5)

def HotwWarmup(onoff) :
    hexdecimal = WatchOption.Hexdecimal
    if onoff == 1 :
        while debugger.Watch.GetValue("F_BLsts2.Bit.b2", hexdecimal) == 0x0 :
            debugger.Watch.SetValue("T_WaitLight", 200)
            debugger.Watch.SetValue("D_SwCom", 0x0d)
            time.sleep(0.5)
    else :
        while debugger.Watch.GetValue("F_BLsts2.Bit.b2", hexdecimal) == 0x1:
            debugger.Watch.SetValue("D_SwCom", 0x0d)
            time.sleep(0.5)

def RsvState(onoff) :
    if onoff == 1 :
        debugger.Watch.SetValue("T_WaitLight", 200)
        debugger.Watch.SetValue("D_RsvState", 0x01)
        time.sleep(0.5)
            
    else :
        debugger.Watch.SetValue("T_WaitLight", 200)
        debugger.Watch.SetValue("D_RsvState", 0x00)
        time.sleep(0.5)

def RsvNum() : # NO. 1~5
    debugger.Watch.SetValue("T_WaitLight", 200)

    Rno = [0x00, 0x01, 0x02, 0x03, 0x04]
    i=0
    for i in Rno :
        debugger.Watch.SetValue("D_RsvNum", i)
        time.sleep(0.5)
    

Set_power(1)
Set_heat(1)
RsvState(1)
RsvNum()
RsvState(0)
Set_HtRapid(1)
Set_HtRapid(0)
Set_wheat(1)
HotwWarmup(1)
HotwWarmup(0)
Set_heat(0)
Set_wheat(0)
Set_power(0)





