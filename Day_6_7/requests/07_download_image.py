import requests

from PIL import Image
from io import BytesIO

r = requests.get("https://media.istockphoto.com/id/814423752/photo/eye-of-model-with-colorful-art-make-up-close-up.jpg?s=612x612&w=0&k=20&c=l15OdMWjgCKycMMShP8UK94ELVlEGvt7GmB_esHWPYE=")

i  = Image.open(BytesIO(r.content))
fp=open("downloaded_image.jpg",'wb')
i.save(fp)
fp.close()