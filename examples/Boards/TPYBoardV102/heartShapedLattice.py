import  pyb
from pyb import Pin

x_row = [Pin(i, Pin.OUT_PP) for i in ['X1','X2','X3','X4','X5','X6','X7','X8']]
y_col = [Pin(i, Pin.OUT_PP) for i in ['Y1','Y2','Y3','Y4','Y5','Y6','Y7','Y8']]

number = [
#第1行
[1,1,1,1,1,1,1,1],
#第2行
[1,0,0,1,1,0,0,1],
#第3行
[0,0,0,0,0,0,0,0],
#第4行
[0,0,0,0,0,0,0,0],
#第5行
[1,0,0,0,0,0,0,1],
#第6行
[1,1,0,0,0,0,1,1],
#第7行
[1,1,1,0,0,1,1,1],
#第8行
[1,1,1,1,1,1,1,1],
]

def displayLED():
    for i,j in enumerate(x_row):
        x_row[i-1].value(0)
        data = number[i]
        for k,l in enumerate(data):
            y_col[k].value(l)
        j.value(1)
        pyb.delay(1)
while 1:
    displayLED()