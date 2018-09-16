from machine import Pin
import network
import time

p2 = Pin(2, Pin.OUT)#8266模块上的小蓝灯

def do_connect():
    sta_if = network.WLAN(network.STA_IF)#设置为STA客户端模式
    sta_if.active(True)# 激活接口
    if not sta_if.isconnected():#检查是否已经连接WIFI网络
        p2.value(1)#高电平熄灭
        print('connecting to network...')
        sta_if.connect('ssid', 'pwd')#连接指定的WIFI网络，传递WIFI名称和密码
        while not sta_if.isconnected():
            pass
    if sta_if.isconnected():
        p2.value(0)#低电平点亮
        print('connect success')
        print('network config:', sta_if.ifconfig())#获取接口的IP/netmask/gw/DNS地址信息

do_connect()