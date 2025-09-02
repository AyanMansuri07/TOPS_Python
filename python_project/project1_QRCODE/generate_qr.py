import qrcode

# This should match your Flask upload route
upload_link = "http://192.168.1.199:5000/upload"

# Generate QR code
qr = qrcode.make(upload_link)

# Save QR code as an image
qr.save("upload_qr.png")

print("✅ QR Code generated: upload_qr.png")
