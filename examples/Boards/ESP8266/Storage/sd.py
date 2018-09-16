#hardware platform:FireBeetle-ESP8266from machine import SPI,Pinimport sdcardimport osspi = SPI(baudrate=100000, polarity=1, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))    #Initialise the SPI bus with the given parameterssd = sdcard.SDCard(spi, Pin(2))     #create sdcard object base spi and Pin2os.mount(sd,"/sd")                  #mount sdcard with specified dirprint(os.listdir('/sd'))            #print the filename in '/sd' dir
fd=open('/sd/dfrobot.txt','rw')     #open file 'dfrobot.txt' in sdcard ,the mode is read and write,and create the file descriptor as fd
fd.write('hello dfrobot')           #write "hello dfrobot" to the file 'dfrobot.txt'
fd.seek(0)                          #move the file pointer to the start
print(fd.read())                    #read from the start of "dfrobot.txt"
fd.close()                          #close file
os.umount("/sd")                    #unmount sdcard