import os
f = open("videos","r")
urls = f.readlines()
for url in urls:
  print "Downloading:",url
  os.system("youtube-dl "+url)

f.close()
