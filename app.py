
import qrcode 

text = input("Enter your qrcode text : ")
filename = input("Enter your filename (.png): ")


qr = qrcode.QRCode(border=1,box_size=10,error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data(text)

qr.make(fit=True)

qrimg = qr.make_image(fill_color="black",back_color="white")

qrimg.show()

qrimg.save(filename)

