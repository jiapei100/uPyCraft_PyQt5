#speaker use board's pin0 and FND
#demo1
import music
music.play(music.NYAN)

'''
#demo2
import music

while True:
  for freq in range(880, 1760, 16):
    music.pitch(freq, 6)
  for freq in range(1760, 880, -16):
    music.pitch(freq, 6)
'''