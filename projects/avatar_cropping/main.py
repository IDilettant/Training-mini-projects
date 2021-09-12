from PIL import Image


image_monroe = Image.open('monro.jpg')
red_channel, green_channel, blue_channel = image_monroe.split()

cutting_width = 50

red_channel_1 = red_channel.crop((cutting_width, 0, red_channel.width, red_channel.height))
red_channel_2 = red_channel.crop((cutting_width / 2, 0, red_channel.width - cutting_width / 2, red_channel.height))
blended_red_channel = Image.blend(red_channel_1, red_channel_2, 0.5)

blue_channel_1 = red_channel.crop((0, 0, blue_channel.width - cutting_width, blue_channel.height))
blue_channel_2 = blue_channel.crop((cutting_width / 2, 0, blue_channel.width - cutting_width / 2, blue_channel.height))
blended_blue_channel = Image.blend(blue_channel_1, blue_channel_2, 0.5)

cropped_green_channel = green_channel.crop((cutting_width / 2, 0, green_channel.width - cutting_width / 2, green_channel.height))

blurry_image = Image.merge('RGB', (blended_red_channel, cropped_green_channel, blended_blue_channel))
blurry_image.save('blurry_image.jpg')
blurry_image.thumbnail((80, 80), Image.ANTIALIAS)
blurry_image.save('blurry_avatar.jpg')
