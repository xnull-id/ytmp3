#Code by XNULL !!!
import os, sys

try:
  url = sys.argv[1]
except:
  print('+---------------------------------------+')
  print('|   YOUTUBE MUSIC DOWNLOADER -- XNULL   |')
  print('|                                       |')
  print('|    ex : python youtube.py <url yt>    |')
  print('+---------------------------------------+')
  sys.exit()

os.system("youtube-dl -x --audio-format mp3 -o 'result/%(title)s.%(ext)s' "+url)
print('\nSUKSES DOWNLOAD !\nResult file > result/hasildonlotmu.mp3')
