import requests

url = "https://assets.mixkit.co/active_storage/sfx/213/213.way"

r = requests.get(url, stream=True)
r.raise_for_status()

totalExpectedBytes = int(r.headers.get("content-length", 0))
bytesreceived = 0

with open("winrar.wav", "wb") as fp:
    for chunk in r.iter_content(chunk_size=128):
        if chunk:
            fp.write(chunk)
            bytesreceived += len(chunk)
            print(f"{bytesreceived} of {totalExpectedBytes} bytes received")
print("Download complete.")