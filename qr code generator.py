import image
import qrcode

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = "https://open.spotify.com/user/31wrsjsduw5wp2bv4ldn7an3oj6i?si=IWRPXztDQ3usUBqVUnhbrQ&utm_source=copy-link"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("test.png")