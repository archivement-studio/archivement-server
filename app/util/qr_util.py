import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import GappedSquareModuleDrawer

import base64

from app.util.pil2byte import pil2byte

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2
)

def qr_generator(url):
    del qr.data_cache
    qr.clear()

    qr.add_data(url)
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer())
    img_byte:bytes = pil2byte(img)
    img_base64 = base64.b64encode(img_byte).decode()
    data_image = 'data:image/png;base64,'+img_base64

    return data_image