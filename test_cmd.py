import time, datetime
hexdecimal = WatchOption.Hexdecimal
Watch = "F_BLsts1.Bit.b4"



while int(debugger.Watch.GetValue(str(Watch), hexdecimal)) != 0 :
    debugger.Watch.SetValue("T_WaitLight", 200)
    debugger.Watch.SetValue("D_SwCom", 0x09)
    time.sleep(0.3)

        

