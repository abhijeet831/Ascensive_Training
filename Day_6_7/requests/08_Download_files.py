import requests

url = "https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-611.exe"
r = requests.get(url)
fp = open("winwar.exe","wb")
fp.write(r.content)
fp.close()