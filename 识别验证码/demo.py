import tesserocr
import urllib.request
from PIL import Image
try:
    file = open('code.png', 'wb')
    file.write(urllib.request.urlopen('http://demo.admin.com//index.php?s=/captcha').read())
    file.close()
    image = Image.open('code.png')
    result = tesserocr.image_to_text(image)
    print(result)
except Exception as e:
    print(e)
