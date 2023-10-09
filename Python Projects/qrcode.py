# Importing library
import qrcode

# Data to be encoded
data = 'QR Code using make() function'

# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save('MyQRCode1.png')
