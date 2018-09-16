from microbit import *
#Please turn microbit in all directions to accomplish calibration without interruption,nor re-download.
#Please accomplish calibration operations or plug and play USB once more if you need to burn the program again. 
compass.calibrate()

while True:
  needle = ((15 - compass.heading()) // 30) % 12
  display.show(Image.ALL_CLOCKS[needle])