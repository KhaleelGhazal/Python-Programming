import pyqrcode
import png
from PIL import Image
link = input("Enter anyling you need a QR code for: ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale = 5)
Image.open("QRCode.png")
