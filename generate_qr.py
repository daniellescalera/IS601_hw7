import qrcode
import os

# Get environment variables for customization
url = os.getenv('QR_DATA_URL', 'https://github.com/daniellescalera')  # Default URL if not provided
output_dir = os.getenv('QR_CODE_DIR', 'qr_codes')
output_filename = os.getenv('QR_CODE_FILENAME', 'github_qr.png')
fill_color = os.getenv('FILL_COLOR', 'black')
back_color = os.getenv('BACK_COLOR', 'white')

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color=fill_color, back_color=back_color)
img.save(os.path.join(output_dir, output_filename))

print(f"QR Code successfully created and saved to {os.path.join(output_dir, output_filename)}")
