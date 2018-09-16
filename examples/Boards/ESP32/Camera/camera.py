#hardware platform: FireBeetle-ESP32#hardware platform: FireBeetle-ESP32from machine import IISfrom machine import Pinimport networkimport time
SSID = "DFROBOT_AP"                     #set wifi idPASSWORD = "12345678"                   #set wifi passwordwlan=Nonecamera = IIS(IIS.CAMERA)                #create a iis object,and set modebutton = Pin(16, Pin.IN)def connectWifi(ssid,passwd):  global wlan  wlan=network.WLAN(network.STA_IF)     #create a wlan object  wlan.active(True)                     #Activate the network interface  wlan.disconnect()                     #Disconnect the last connected WiFi  wlan.connect(ssid,passwd)             #connect wifi  while(wlan.ifconfig()[0]=='0.0.0.0'):    time.sleep(1)
connectWifi(SSID,PASSWORD)   camera.init()                           #init cameracamera.setFramesize(IIS.HQVGA)          #set frameratecamera.setPixformat(IIS.GRAYSCALE)      #set pix formatcamera.httpServerStart()                #open http server
#Catch exceptions,stop camera if interrupted accidentallytry:
  while True:    pass
except:
  camera.httpServerStop()   wlan.disconnect()
