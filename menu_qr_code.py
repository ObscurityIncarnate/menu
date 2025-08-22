import qrcode
from PIL import Image
# Your website
url = "https://obscurityincarnate.github.io/menu/"

# Generate QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill="black", back_color="white")


# # If you want to add a logo at the center of the QR code, uncomment the following lines and provide a logo image
# qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
# logo = Image.open('ksf_place_design_logo.png')

# # Convert logo to RGBA (if it has transparency)
# if logo.mode != "RGBA":
#     logo = logo.convert("RGBA")

# # Create a mask for transparency
# mask = logo.split()[3]  # Take the alpha channel

# # Resize logo to fit in QR code (usually 20–30% of QR size)
# qr_width, qr_height = qr_img.size
# logo_size = qr_width // 4  # 25% of QR code
# logo = logo.resize((logo_size, logo_size))

# #positioning the logo at the center
# pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
# qr_img.paste(logo, pos, mask=logo)

# qr_img.save("menu_qr_with_logo.png")

img.save("menu_qr.png")
