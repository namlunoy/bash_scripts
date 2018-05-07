import urllib

link = "https://store.liverpoolfc.com/kit/away-kit/kids/"
f = urllib.urlopen(link)
myfile = f.read()
print myfile
