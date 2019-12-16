import qrtools
qr = qrtools.QR()
qr.decode("/home/aminul/a.jpeg")
print (qr.data)
