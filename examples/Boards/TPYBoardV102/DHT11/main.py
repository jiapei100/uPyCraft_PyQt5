# main.py -- put your code here!
from dht11 import DHT11
from pyb import Pin

dht = DHT11('Y8')

#数码管a~g dp对应的开发板引脚
d_Pins=[Pin(i,Pin.OUT_PP) for i in ['X1','X2','X3','X4','X5','X6','X7','X8']]
#数码管位段1 2 3 4对应的引脚
w_Pins=[Pin(i,Pin.OUT_PP) for i in ['Y9','Y10','Y11','Y12']]
data = '0000' #初始化数码管显示0

number={
'0':
[0,0,0,0,0,0,1,1],#0
'1':
[1,1,1,1,0,0,1,1],#1
'2':
[0,0,1,0,0,1,0,1],#2
'3':
[0,0,0,0,1,1,0,1],#3
'4':
[1,0,0,1,1,0,0,1],#4
'5':
[0,1,0,0,1,0,0,1],#5
'6':
[0,1,0,0,0,0,0,1],#6
'7':
[0,0,0,1,1,1,1,1],#7
'8':
[0,0,0,0,0,0,0,1],#8
'9':
[0,0,0,0,1,0,0,1],#9
}
def display(num,dp):
    global number
    data = number[num]
    for count,pin in enumerate(d_Pins):#显示num的值
        pin.value(data[count])

def clear():
    for i in w_Pins:
        i.value(0)
    for i in d_Pins:
        i.value(1)
def showData(num):

    for i,k in enumerate(num):
        pyb.delay(1)
        clear()
        w_Pins[3-i].value(1)
        display(k,0)

while True:
    data = dht.read_data()#读取温湿度的值
    print('温度:',data[0],'湿度:',data[1])
    #让数码管持续显示一段时间
    for i in range(1500):
        #前两位显示温度 后两位显示湿度
        showData(str(data[0])+str(data[1]))
