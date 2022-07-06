from captcha.image import ImageCaptcha
import datetime
import random

image = ImageCaptcha(width=280, height= 90)
material = "123456789qwertyuiopasdfghjklzxcvbnm"
output = "".join(random.sample(material,5))
captcha_text = output
data = image.generate(captcha_text)
time_stamp = datetime.datetime.now().strftime('%b-%d-%Y_%I-%M-%S')
file_name = f'Captcha {time_stamp}.png'
image.write(captcha_text, file_name)
print(output)