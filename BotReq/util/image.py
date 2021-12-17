import urllib.request

def downloadImage(url,path):
    urllib.request.urlretrieve(url,path)