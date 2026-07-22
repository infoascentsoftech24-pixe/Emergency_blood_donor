import qrcode


# =============================
# BloodCare Registration URL
# =============================

# Replace this IP address with your laptop IPv4 address
# Example: http://192.168.1.25:5000/register

url = "http://10.252.111.140/register"



# =============================
# CREATE QR CODE
# =============================

qr = qrcode.QRCode(

    version=1,

    error_correction=qrcode.constants.ERROR_CORRECT_L,

    box_size=10,

    border=4

)


qr.add_data(url)

qr.make(fit=True)



# Generate image

qr_image = qr.make_image()



# Save QR

qr_image.save("bloodcare_registration_qr.png")



print("=================================")

print("BloodCare QR Generated Successfully")

print("Scan URL:")

print(url)

print("Saved as: bloodcare_registration_qr.png")

print("=================================")