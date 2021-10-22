import qrcode
import uuid
import os
dirname =os.path.dirname(__file__)
filename = os.path.join(dirname,'..\\qr_codes\\')

def link_to_qr(link):
    img = qrcode.make(link)
    name = str(uuid.uuid4())
    path = filename+f"{name}.png"
    img.save(path)
    return path
print(link_to_qr('https://pypi.org/project/pyTelegramBotAPI/0.3.0/'))    