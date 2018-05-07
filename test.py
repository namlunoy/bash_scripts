import requests

link = "https://store.liverpoolfc.com/kit/away-kit/kids/"
f = requests.get(link)

print f.text
