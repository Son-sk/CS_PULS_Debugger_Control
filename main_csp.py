from heat import Set_heat, Set_wheat, Set_power, Set_HtRapid, HotwWarmup, RsvState, RsvNum


if __name__ == "__main__":
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
    Set_power(1)
