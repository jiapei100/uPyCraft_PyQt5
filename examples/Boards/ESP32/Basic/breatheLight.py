#Hardware Platform: FireBeetle-ESP32#Result: Press the button and LED is ON, release the button and LED is OFF.#Hardware Connection: this test needs to connect to an external button module in IO27 and an external LED module in IO25. #The info below shows that digitalRead is available for the current version.#button:IO2  IO4  IO5  IO10  IO12~19  IO23  IO25~27  IO34~36  IO39#led:   IO0  IO4  IO10 IO12~19  IO21~23  IO25~27#Except the connection between IO2 and onboard LED, other pins need to connect to external LEDs.
from machine import Pin,Timer,PWM
pwm =PWM(Pin(2),100)      #create PWM object from a pin,and set frequency
polar = 0
duty = 0
def setLed(t):            #create a variate,and change it between 0 and 1008
  global duty,polar
  if(polar == 0):
    duty+=16
    if(duty >= 1008):
      polar = 1
  else:
    duty -= 16
    if(duty <= 0):
      polar = 0
  pwm.duty(duty)           #set duty of the PWM
tim = Timer(1)             #create Timer object from Virtual timers with timer ID=1
tim.init(period=10,mode=Timer.PERIODIC, callback=setLed) #init Timer,Call the callback function with per second#Catch exceptions,stop program if interrupted accidentally in the 'try'
try:                       #The catching
  while True:
    pass
except:                    #Capture anomaly, deinit Timer and PWM
  tim.deinit()
  pwm.deinit()
