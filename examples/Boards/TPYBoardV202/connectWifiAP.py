import network

#将TPYBoard v202设置成AP模式
ap_if = network.WLAN(network.AP_IF)
#激活接口
ap_if.active(True)
#开放WIFI。名称:TPYBoard v202 密码:12345678
ap_if.config(essid='TPYBoard v202',password='12345678')