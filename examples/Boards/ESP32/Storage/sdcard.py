#hardware platform:FireBeetle-ESP32import SDimport ossd = SD.sdcard()                    #create sdcard objectos.mount(sd,"/sd")                  #mount sdcard with specified dirprint(os.listdir("/sd"))            #print the filename in '/sd' dirf=open("sd/HelloWord.txt","w")      #open file 'HelloWord.txt' in sdcard 
f.write("HelloWord!!!")             #write "HelloWord!!!" to the file
f.close()                           #close file

f=open("sd/HelloWord.txt","r")      #open file 'HelloWord.txt' in sdcard print(f.read())                     #read data from file
f.close()os.umount("/sd")                    #unmount sdcard