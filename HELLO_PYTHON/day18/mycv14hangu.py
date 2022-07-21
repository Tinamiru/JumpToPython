import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

img = cv2.imread("startup.png")

color_coverted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_pil = Image.fromarray(color_coverted)

draw = ImageDraw.Draw(img_pil)
draw.text((450, 150), "수지", font=ImageFont.truetype("./HMKMM.TTF", 48), fill=(0, 0, 0))

numpy_img = np.array(img_pil)
cv_img = cv2.cvtColor(numpy_img, cv2.COLOR_RGB2BGR)

cv2.imshow("test", cv_img)
cv2.waitKey()
