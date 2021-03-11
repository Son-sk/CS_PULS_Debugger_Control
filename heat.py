import time, datetime
# hexdecimal = WatchOption.Hexdecimal
# Watch = "F_BLsts1.Bit.b4"
#F_DspMode.Bit.b0

def Set_heat(onoff) :
    hexdecimal = WatchOption.Hexdecimal
    if onoff == 1 :
        while int(debugger.Watch.GetValue("D_BoilOper", hexdecimal)) != 0x30 and int(debugger.Watch.GetValue("D_BoilOper", hexdecimal)) != 0x20   :
            debugger.Watch.SetValue("F_OneshotSw.Bit.b4", 1)
            debugger.Watch.SetValue("T_WaitLight", 200)
            time.sleep(1)
    else :
        while int(debugger.Watch.GetValue("D_BoilOper", hexdecimal)) == 0x30 or int(debugger.Watch.GetValue("D_BoilOper", hexdecimal)) == 0x20 :
            debugger.Watch.SetValue("F_OneshotSw.Bit.b4", 1)
            debugger.Watch.SetValue("T_WaitLight", 200)
            time.sleep(1)


def Set_wheat(onoff) :
    hexdecimal = WatchOption.Hexdecimal
    if onoff == 1 :
        while int(debugger.Watch.GetValue("D_BoilOper", hexdecimal)) != 0x30 and int(debugger.Watch.GetValue("D_BoilOper", hexdecimal)) != 0x10   :
            debugger.Watch.SetValue("F_OneshotSw.Bit.b1", 1)
            debugger.Watch.SetValue("T_WaitLight", 200)
            time.sleep(1)
    else :
        while int(debugger.Watch.GetValue("D_BoilOper", hexdecimal)) == 0x30 or int(debugger.Watch.GetValue("D_BoilOper", hexdecimal)) == 0x10 :
            debugger.Watch.SetValue("F_OneshotSw.Bit.b1", 1)
            debugger.Watch.SetValue("T_WaitLight", 200)
            time.sleep(1)


def Set_power(onoff) :
    hexdecimal = WatchOption.Hexdecimal
    if onoff == 1 :
        while int(debugger.Watch.GetValue("M_SWStep", hexdecimal)) == 0x00 :
            debugger.Watch.SetValue("T_WaitLight", 200)
            debugger.Watch.SetValue("D_SwCom", 0x01)
            time.sleep(0.5)
    else :
        while int(debugger.Watch.GetValue("M_SWStep", hexdecimal)) > 0x00 :
            debugger.Watch.SetValue("D_SwCom", 0x02)
            time.sleep(0.5)


Set_power(1)

Set_heat(1)
Set_wheat(1)
Set_heat(0)
Set_wheat(0)

Set_power(0)
Set_power(1)




