#Audio captcha generator
from captcha.audio import AudioCaptcha
audio = AudioCaptcha()
captcha_text = "909089"
audiolevel = audio.generate(captcha_text)
audio_file = "audio" + captcha_text + ".wav"
audio.write(captcha_text, audio_file)


#Image captcha generator
from captcha.image import ImageCaptcha
image = ImageCaptcha(width = 200, height = 30)
captchaText = input("Enter the captcha text: ")
data = image.generate(captchaText)
image.write(captchaText, "CAPTCHA.png")
from PIL import Image
Image.open("CAPTCHA.png")
