
	#define	f_MenuOsSw			(F_OneshotSw.Bit.b0)	/*		메뉴 sw	*/
	#define	f_HotwOsSw			(F_OneshotSw.Bit.b1)	/*		온수 sw	*/
	#define	f_HwupOsSw			(F_OneshotSw.Bit.b2)	/*		온수 up sw	*/
	#define	f_HwdnOsSw			(F_OneshotSw.Bit.b3)	/*		온수 down sw	*/
	#define	f_HeatOsSw			(F_OneshotSw.Bit.b4)	/*		난방 sw	*/
	#define	f_HtupOsSw			(F_OneshotSw.Bit.b5)	/*		난방 up sw	*/
	#define	f_HtdnOsSw			(F_OneshotSw.Bit.b6)	/*		난방 down sw	*/
	#define	f_AutoSavOsSw		(F_OneshotSw.Bit.b7)	/*		auto/save sw	*/
	#define	f_HwCupsw			(F_OneshotSw.Bit.b8)	//		온수 up 연속 sw
	#define	f_HwCdnsw			(F_OneshotSw.Bit.b9)	//		온수 down 연속 sw
	#define	f_HtCupsw			(F_OneshotSw.Bit.b10)	//		난방 up 연속 sw
	#define	f_HtCdnsw			(F_OneshotSw.Bit.b11)	//		난방 down 연속 sw

    # /*	보일러 상태 정보
	# - bit0 : 온수 설정 온도 (최상위 bit)
	# - bit1 : 난방대기 (0 : 가동, 1 : 대기)
	# - bit2/bit3 : 연소 샹태 (00 : 소화중, 10 : 온수연소, 01 : 난방연소, 11 : 동방연소)
	# - bit4 : 난방운전제어모드 (0 : 온돌, 1 : 실온)
	# - bit5 : 동결 경보 알림 (0 : 동결 th ＞ 0℃, 1 : 동결 th ≤ 0℃)
	# - bit6 : 온수급수표시 (0 : 수류 off, 1 : 수류 on
	# - bit7 : 동결방지운전상태 (0 : 일반, 1 : 동결)	*/
	# F_BLsts1.Byte = ((BI_MainRecv[2] >> 1) & 0x0f) | ((BI_MainRecv[4] << 3) & 0xf0);
	# 													/*	boiler 상태 정보 set	*/