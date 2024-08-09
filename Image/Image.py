from PIL import Image
from PIL import ImageFilter

image = Image.open('image.png')
image.save('./Image/hasil1.jpg')

cropped_image = image.crop((10, 10, 150, 150))
cropped_image.save('./Image/hasilcrop.jpg')

resized_image = image.resize((700, 500))
resized_image.save('./Image/hasilresize.jpg')

filtered_image = resized_image.filter(ImageFilter.FIND_EDGES)
filtered_image.save('./Image/hasilfilter1.jpg')
filtered_image = resized_image.filter(ImageFilter.CONTOUR)
filtered_image.save('./Image/hasilfilter2.jpg')
