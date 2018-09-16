try:
    import usocket as socket
except:
    import socket
import network,time,onewire,ds18x20
from machine import Pin


html="""
<!DOCTYPE html>
<html>
    <head> <title>TPYBoard v202 IOT Test</title> </head>
    <body> 
    <center>
    <h1>TPYBoard v202 IOT Test</h1>
         <form action="/" method="get" accept-charset="utf-8">
                <p>温度:&nbsp; %s &nbsp;<input type="Submit" value="r" name="temp" /></p>  
                <p>继电器:&nbsp; %s <input type="Submit" value="1" name="relay" />&nbsp;<input type="Submit" value="0" name="relay" /></p>         
                
            </form>
    </center>
    </body>
</html>
"""
#初始化
def InitGPIO():
    #继电器低电平触发，低电平时COM和NO会闭合
	Relay.value(1)
	Light.value(1)

def GetTemp():
	roms = ds.scan()#扫描总线上的设备
	ds.convert_temp()#获取采样温度
	time.sleep_ms(750)
	_val=0
	for rom in roms:
		_val=ds.read_temp(rom)#得到温度
	return _val
def OpenNetwork(essid,pwd):
	ap_if = network.WLAN(network.AP_IF)#建立AP模式
	ap_if.active(True)
	ap_if.config(essid=essid, authmode=network.AUTH_WPA_WPA2_PSK, password=pwd)
	ap_if.ifconfig()
	
def StartServer():
	global html
	
	s = socket.socket()
	addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(addr)
	s.listen(5)

	while True:
		res = s.accept()
		client_s = res[0]
		client_addr = res[1]
		Light.value(1)
		req =client_s.readline()
		while True:
			h = client_s.readline()
			if h == b"" or h == b"\r\n":
				break
			req+=(h.decode('utf-8'))
		print("Request:")
		req=req.lower()
		req=req.decode('utf-8').split('\r\n')
		#http header 解析
		req_data=req[0].lstrip().rstrip().replace(' ','')
		print(req_data)
		if req_data.find('favicon.ico')>-1:
			client_s.close()
			continue
		else:
			temp_val = ''
			req_data=req_data.replace('get/?','').replace('http/1.1','')
			#判断是否是控制继电器
			_index=req_data.find('relay=')
			if _index>-1:
				
				_val=req_data[_index+6:_index+7].lstrip().rstrip()
				print('relay:',_val)
				Relay.value(int(_val))
			#判断是否是获取温度的
			_index=req_data.find('1=')
			if _index>-1:
				s_data=dev_data
				_val=req_data[_index+5:_index+6].lstrip().rstrip()
				print('temp:',_val)
				if _val=='r':
					temp_val=GetTemp()
			response = html % (temp_val,str(Relay.value()))
			print('-----------')
			client_s.send(response)
			client_s.close()
		Light.value(0)
if __name__=='__main__':
	#板子上的蓝灯 高电平:灭 低电平:亮
	Light = Pin(2, Pin.OUT)
	#继电器控制引脚
	Relay = Pin(5, Pin.OUT)
	#创建总线 引脚4 用于DS18B20
	ow=onewire.OneWire(Pin(4))
	ds=ds18x20.DS18X20(ow)

	InitGPIO()
	OpenNetwork('tpyboardv202',b'12345678')
	StartServer()