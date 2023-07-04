from django.db import models
from distutils.command.upload import upload
import qrcode 
from io import BytesIO
from django.core.files import File
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


class QRCode(models.Model):
    name =models.CharField(max_length=250)
    qr_code =models.ImageField(upload_to='qr_code/', blank=True, null=True)


    def __str__(self):
        return str(self.name)


    def save(self, *args, **kwargs):
        QRCode =qrcode.QRCode()
        QRCode.add_data(self.name)
        QRCode.make()
        QRImg =QRCode.make_image(
            image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),
            color_mask=RadialGradiantColorMask()
        )

        fname =f'qr-code{self.id}.png'
        buffer = BytesIO()
        QRImg.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save =False)
        QRImg.close()

        super().save(*args, **kwargs)
